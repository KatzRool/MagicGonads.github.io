#Master
master_atoms = []
master_comps = []
master_moles = []
#Atom
class atom:
    #Meta
    meta_symbols = ['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Uut','Fl','Uup','Lv','Uus','Uuo']
    meta_periods = [0,1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    meta_groups = [0,1, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    meta_weight = [0,1.00794, 4.002602, 6.94, 9.0121831, 10.81, 12.011, 14.007, 15.999, 18.998403163, 20.1797, 22.98976928, 24.305, 26.9815385, 28.085, 30.973761998, 32.06, 35.45, 39.948, 39.0983, 40.078, 44.955908, 47.867, 50.9415, 51.9961, 54.938044, 55.845, 58.933194, 58.6934, 63.546, 65.38, 69.723, 72.63, 74.921595, 78.971, 79.904, 83.798, 85.4678, 87.62, 88.90584, 91.224, 92.90637, 95.95, 98.0, 101.07, 102.9055, 106.42, 107.8682, 112.414, 114.818, 118.71, 121.76, 127.6, 126.90447, 131.293, 132.90545196, 137.327, 138.90547, 140.116, 140.90766, 144.242, 145.0, 150.36, 151.964, 157.25, 158.92535, 162.5, 164.93033, 167.259, 168.93422, 173.045, 174.9668, 178.49, 180.94788, 183.84, 186.207, 190.23, 192.217, 195.084, 196.966569, 200.592, 204.38, 207.2, 208.9804, 209.0, 210.0, 222.0, 223.0, 226.0, 227.0, 232.0377, 231.03588, 238.02891, 237.0, 244.0, 243.0, 247.0, 247.0, 251.0, 252.0, 257.0, 258.0, 259.0, 266.0, 267.0, 268.0, 269.0, 270.0, 269.0, 278.0, 281.0, 282.0, 285.0, 286.0, 289.0, 289.0, 293.0, 294.0, 294.0]
    meta_elements = ['','Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Ununtrium', 'Flerovium', 'Ununpentium', 'Livermorium', 'Ununseptium', 'Ununoctium']
    meta_proton = 1.67226*10**-27
    meta_neutron = 1.6929*10**-27
    meta_electron = 9.11*10**-31
    #Func
    #Self
    def bond(self,atom,bonds=0,form=0):
        if bonds == 0:
            bonds = min(abs(self.charge),abs(atom.charge))
        if form == 0:
            form = abs(self.charge)/(self.charge+(self.charge==0))
        self.charge-=bonds*form
        atom.charge+=bonds*form
        if atom not in self.bonds:
            self.bonds[atom] = -bonds*form
            atom.bonds[self] = bonds*form
        else:
            self.bonds[atom] -= bonds*form
            atom.bonds[self] += bonds*form
        self.electrons = self.number - self.charge
        atom.electrons = atom.number - atom.charge
    #Init
    def __init__(self,number=0,charge=0,isotope=0):
        self.id = len(master_atoms)
        self.bonds = {}
        self.symbol = atom.meta_symbols[number]
        self.name = atom.meta_elements[number]
        self.period = atom.meta_periods[number]
        self.group = atom.meta_groups[number]
        self.weight = atom.meta_weight[number]
        if isotope == 0:
            isotope = round(12*self.weight/atom.meta_weight[6])
        self.isotope = isotope
        self.number = number
        self.charge = charge
        self.protons = number
        self.neutrons = isotope-number
        self.electrons = number-charge
        self.mass = number*(atom.meta_proton)+self.neutrons*(atom.meta_neutron)
        master_atoms.append(self)
    @classmethod
    def element(cls,symbol='',charge=0,isotope=0):
        return cls(atom.meta_symbols.index(symbol),charge,isotope)
#Compounds
class comp:
    #Meta
    #Func
    #Self
    def bond(self,comp,bonds=0,form=0):
        if bonds == 0:
            bonds = min(abs(self.charge),abs(comp.charge))
        if form == 0:
            form = abs(self.charge)/(self.charge+(self.charge==0))
        self.charge-=bonds*form
        comp.charge+=bonds*form
        if atom not in self.bonds:
            self.bonds[comp] = -bonds*form
            comp.bonds[self] = bonds*form
        else:
            self.bonds[comp] -= bonds*form
            comp.bonds[self] += bonds*form
    #Init
    def __init__(self,*atoms):
        for i in range(1,len(atoms)):
            atoms[i-1].bond(atoms[i])
        self.atoms = atoms
        self.bonds = {}
        self.mass = 0
        self.weight = 0
        self.charge = 0
        for x in self.atoms:
            self.mass += x.mass
            self.weight += x.weight
            self.charge += x.charge
        master_comps.append(self)
#Molecule
class mole:
    #Meta
    #Func
    #Self
    def bond(self,mole,bonds=0,form=0):
        if bonds == 0:
            bonds = min(abs(self.charge),abs(mole.charge))
        if form == 0:
            form = abs(self.charge)/(self.charge+(self.charge==0))
        self.charge-=bonds*form
        comp.charge+=bonds*form
        if atom not in self.bonds:
            self.bonds[mole] = -bonds*form
            mole.bonds[self] = bonds*form
        else:
            self.bonds[mole] -= bonds*form
            mole.bonds[self] += bonds*form
    def ionic(self,other):
        if self.charge > other.charge:
            ion = self
            anion = other
        else:
            ion = other
            anion = self
        #return
        pass
    #Init
    def __init__(self,*compounds):
        self.mass = 0
        self.weight = 0
        self.charge = 0
        for x in self.atoms:
            self.mass += x.mass
            self.weight += x.weight
            self.charge += x.charge
        master_moles.append(self)
