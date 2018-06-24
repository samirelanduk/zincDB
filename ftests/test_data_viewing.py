from .base import FunctionalTest

class PdbPageTests(FunctionalTest):

    def test_pdb_page_layout(self):
        # User goes to PDB page
        self.get("/pdbs/A001/")
        self.check_title("A001")
        self.check_h1("A SUPERB PDB FILE")

        # There is information about the PDB
        pdb_information = self.browser.find_element_by_id("pdb-info")
        self.assertIn("Deposition Date: 28 September, 1990", pdb_information.text)
        self.assertIn("Classification: REDUCTASE", pdb_information.text)
        self.assertIn("Technique: X-RAY", pdb_information.text)
        self.assertIn("Source Organism: Felis catus", pdb_information.text)
        self.assertIn("Expression System: Escherichia coli BL21(DE3)", pdb_information.text)
        self.assertIn("Resolution: 2.1 Å", pdb_information.text)
        self.assertIn("R-factor: 4.5 Å", pdb_information.text)
        self.assertIn("Code: A001", pdb_information.text)

        # There is an overview of the PDB's chains
        chain_information = self.browser.find_element_by_id("pdb-chains")
        self.assertIn("2 zinc-bearing chains (A, B)", chain_information.text)

        # There is an overview of the PDB's zinc sites
        site_information = self.browser.find_element_by_id("pdb-sites")
        self.assertIn("2 zinc binding sites", site_information.text)
        sites = site_information.find_elements_by_class_name("pdb-site")
        self.assertEqual(len(sites), 2)
        self.assertIn("A0014003", sites[0].text)
        self.assertIn("3 residues", sites[0].text)
        self.assertIn("A21 (TYR), A23 (TYR), A25 (VAL)", sites[0].text)
        self.assertIn("A0018003", sites[1].text)
        self.assertIn("3 residues", sites[1].text)
        self.assertIn("B23 (TYR), B25 (VAL), B500 (HOH)", sites[1].text)

        # There is a 3D display
        ngl = self.browser.find_element_by_id("pdb-ngl")


    def test_pdb_page_displays_angstroms_properly(self):
        # User goes to PDB page
        self.get("/pdbs/A002/")
        self.check_title("A002")
        self.check_h1("A FINE PDB FILE")

        # No resolution or rfactor is shown
        pdb_information = self.browser.find_element_by_id("pdb-info")
        self.assertIn("Technique: NMR", pdb_information.text)
        self.assertIn("Resolution: N/A", pdb_information.text)
        self.assertIn("R-factor: N/A", pdb_information.text)


    def test_404_on_no_pdb(self):
        self.get("/pdbs/XXX/")
        self.check_title("Not Found")



class ZincSitePageTests(FunctionalTest):

    def test_pdb_page_layout(self):
        # User goes to site page
        self.get("/A0014003/")
        self.check_title("A0014003")
        self.check_h1("A0014003")

        # There is an info section
        info = self.browser.find_element_by_id("site-info")
        metals = info.find_elements_by_class_name("metal")
        self.assertEqual(len(metals), 1)
        residues = info.find_elements_by_class_name("residue")
        self.assertEqual(len(residues), 3)
        self.assertIn("A21 (TYR) A23 (TYR) A25 (VAL)", info.text)
        self.assertIn("ZN", info.text)


    def test_404_on_no_site(self):
        self.get("/XXXXXXX/")
        self.check_title("Not Found")
