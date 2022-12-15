""" Build a database of energy sources in the US. """
import sqlite3
import sys
from argparse import ArgumentParser

""" The EnergyDB class has a method to calculate the total energy production by source and year. I use this method to determine how much electricity was generated from solar and wind energy in 2017. This class inludes __init__, __del__, read and production_by_source methods to help me achieve this. """

def EnergyDB():
    """ This object let's the class initailize its attributes with the parameters lef and filename """
    def __init__(self, filename):
        self.conn = sqlite3.connect(':memory:')
        self.read(filename)

    """ The purpose of this method is to close the database connection when an EnergyDB object is destroyed (for example, when your program ends) """
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass
        
    """ This method has two parameters and uses the Cursor object to create a new table called production. It also opens one of the parameters for reading, making sure the application ignores the first line in the file, which are the column headers. This also makes sure that the year is converted to an integer and the megawatt hours are converted to a float. I the commit my changes to the database """
    def read(self, filename):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE production(year integer, state text, source text, mwh real")
        with open(filename, "r" , encoding = "utf-8") as f:
            lines = f. readlines()[1:]
            for line in lines:
                read.split_list = line.strip().split(',')
                Year=int(Year)
                Megawatthours=float(Megawatthours)
            self.cursor.execute("INSERT INTO production VALUES (?,?,?,?)")  
        read.cursor.commit()
        read.cursor.close()

    """ This method has three parameters and includes a Cursor object ti my database connection. I then fetch all the values returned by this statement, add them together, and return the total """
    def production_by_source(self, source, year):
        cursor = self.conn.cursor()
        cursor.execute("SELECT mwh FROM production WHERE source=? AND year=?")  
        print(cursor.fetchall(production_by_source))   

def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)