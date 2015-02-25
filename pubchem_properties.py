__author__ = 'sjc294'

import pubchempy as pcp
import tkinter, tkinter.filedialog


def print_properties(comp, filepath):
    out_content = [comp.cid,
                     comp.record,
                     comp.atoms,
                     comp.bonds,
                     comp.elements,
                     comp.synonyms,
                     comp.sids,
                     comp.aids,
                     comp.coordinate_type,
                     comp.charge,
                     comp.molecular_formula,
                     comp.molecular_weight,
                     comp.canonical_smiles,
                     comp.isomeric_smiles,
                     comp.inchi,
                     comp.inchikey,
                     comp.iupac_name,
                     comp.xlogp,
                     comp.exact_mass,
                     comp.monoisotopic_mass,
                     comp.tpsa,
                     comp.complexity,
                     comp.h_bond_donor_count,
                     comp.h_bond_acceptor_count,
                     comp.rotatable_bond_count,
                     comp.fingerprint,
                     comp.heavy_atom_count,
                     comp.isotope_atom_count,
                     comp.atom_stereo_count,
                     comp.defined_atom_stereo_count,
                     comp.undefined_atom_stereo_count,
                     comp.bond_stereo_count,
                     comp.defined_bond_stereo_count,
                     comp.undefined_bond_stereo_count,
                     comp.covalent_unit_count]
    with open(file_path, 'ab+') as my_out:
        my_out.write()

if __name__ == "__main__":

    root = tkinter.Tk()
    root.withdraw()

    file_path = tkinter.filedialog.askopenfilename()

    with open(file_path) as f:
        l = f.readlines()

    for idx in l:
        c = pcp.Compound.from_cid(idx)
        print_properties(c,'pubchem_properties.txt')