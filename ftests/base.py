import os
import sys
from time import sleep
from datetime import datetime, timedelta
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from zincbind.models import Pdb, Residue, ZincSite, Atom

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        # Create 8 Pdbs
        pdb_codes = [
         "{}AA{}".format(n, chr(c + 65)) for n in range(1, 3) for c in range(4)
        ]
        for index, code in enumerate(pdb_codes):
            if index not in [1, 3, 6]:
                Pdb.objects.create(pk=code, checked=datetime.now())
            else:
                day = datetime(2012, 1, 1) + timedelta(days=index)
                Pdb.objects.create(
                 id=code, checked=datetime.now(),
                 title="PDB {}".format(index + 1), deposited=day,
                 resolution=5-(index / 10), rfactor=10-(index / 5),
                 technique="X RAY" if index == 1 else "NMR",
                 organism="HOMO SAPIENS" if index == 3 else "MUS MUSCULUS",
                 expression="E. COLI",
                 classification="IMMUNOGLOBULIN" if index == 6 else "LYASE"
                )

        site1 = ZincSite.objects.create(
         id=pdb_codes[1] + "A100", x=1.5, y=2.5, z=2.5,
         pdb=Pdb.objects.get(pk=pdb_codes[1])
        )
        for r in range(11, 14):
            residue = Residue.objects.create(
             id=pdb_codes[1] + "A" + str(r), residue_id="A" + str(r),
             name="VAL" if r % 2 else "CYS", number=r, chain="A"
            )
            for a in range(1, 5):
                Atom.objects.create(
                 id=pdb_codes[1] + str(a + r * 10), x=a, y=a, z=a, charge=0, bfactor=1.5,
                 name=str(a), element="C", atom_id=a + r * 10, residue=residue,
                 alpha=(a == 1), beta=(a == 2), liganding=(a > 2)
                )
            site1.residues.add(residue)

        site2 = ZincSite.objects.create(
         id=pdb_codes[3] + "A200", x=1.5, y=2.5, z=2.5,
         pdb=Pdb.objects.get(pk=pdb_codes[3])
        )
        for r in range(11, 14):
            residue = Residue.objects.create(
             id=pdb_codes[3] + "A" + str(r), residue_id="A" + str(r),
             name="VAL" if r % 2 else "CYS", number=r, chain="A"
            )
            for a in range(1, 5):
                Atom.objects.create(
                 id=pdb_codes[3] + str(a + r * 10), x=a, y=a, z=a, charge=0, bfactor=1.5,
                 name=str(a), element="C", atom_id=a + r * 10, residue=residue,
                 alpha=(a == 1), beta=(a == 2), liganding=(a > 2)
                )
            site2.residues.add(residue)
        site3 = ZincSite.objects.create(
         id=pdb_codes[3] + "B200", x=1.5, y=2.5, z=2.5,
         pdb=Pdb.objects.get(pk=pdb_codes[3])
        )
        for r in range(11, 14):
            residue = Residue.objects.create(
             id=pdb_codes[3] + "B" + str(r), residue_id="B" + str(r),
             name="VAL" if r % 2 else "CYS", number=r, chain="B"
            )
            for a in range(1, 5):
                Atom.objects.create(
                 id=pdb_codes[3] + str(a + r * 100), x=a, y=a, z=a, charge=0, bfactor=1.5,
                 name=str(a), element="C", atom_id=a + r * 100, residue=residue,
                 alpha=(a == 1), beta=(a == 2), liganding=(a > 2)
                )
            site3.residues.add(residue)

        site4 = ZincSite.objects.create(
         id=pdb_codes[6] + "E500", x=1.5, y=2.5, z=2.5,
         pdb=Pdb.objects.get(pk=pdb_codes[6])
        )
        for r in range(11, 14):
            residue = Residue.objects.create(
             id=pdb_codes[6] + "E" + str(r), residue_id="E" + str(r),
             name="VAL" if r % 2 else "CYS", number=r, chain="E"
            )
            for a in range(1, 5):
                Atom.objects.create(
                 id=pdb_codes[6] + str(a + r * 100), x=a, y=a, z=a, charge=0, bfactor=1.5,
                 name=str(a), element="C", atom_id=a + r * 100, residue=residue,
                 alpha=(a == 1), beta=(a == 2), liganding=(a > 2)
                )
            site4.residues.add(residue)



class BrowserTest(FunctionalTest):

    def setUp(self):
        FunctionalTest.setUp(self)
        self.headless = os.environ.get("djangovar") == "headless"
        if self.headless:
            self.browser = webdriver.PhantomJS()
        else:
            try:
                self.browser = webdriver.Chrome()
            except:
                self.browser = webdriver.Firefox()
        self.browser.set_window_size(800, 700)


    def tearDown(self):
        self.browser.quit()
        try:
            os.remove("ghostdriver.log")
        except IOError: pass


    def get(self, url):
        self.browser.get(self.live_server_url + url)


    def check_page(self, url):
        self.assertEqual(self.browser.current_url, self.live_server_url + url)


    def check_title(self, text):
        self.assertIn(text, self.browser.title)


    def check_h1(self, text):
        self.assertIn(text, self.browser.find_element_by_tag_name("h1").text)


    def scroll_to(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)


    def click(self, element):
        self.scroll_to(element)
        element.click()
        sleep(0.5)