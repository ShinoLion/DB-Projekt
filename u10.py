import psycopg2
import pandas
import matplotlib.pyplot as plt

def visualize():
	
	check = "J"
	countries =[]
	years = []
	while check == "J":
		c = input("Über welches Land möchten Sie etwas wissen? [ENG]")
		countries.append(c)
		check = input("Darf es noch ein Land sein? [J/N]")
	
	check ="J"
	while check == "J":
		y = input("In welchem Jahr? [2005-2019]")
		years.append(y)
		check = input("Noch weitere Jahre hinzufügen? [J/N]")
		
	c = psycopg2.connect("dbname=Projekt user=postgres password=abgehn")
	cur = c.cursor()
	
	while countries !=[]:
		elem = countries.pop(0)
		elem = str(elem)
		temp = years.copy()
		while temp != []:
			elem2 = temp.pop(0)
			cur.execute("INSERT INTO chosen (countries, years) VALUES (%s, %s)",(elem, elem2))
		
	
	# keine commits, damit wir die Tabelle immer wieder leer haben

	
	df = pandas.read_sql("SELECT CONCAT(\"Location\",\"years\") AS \"RES\", \"Value\"  AS \"Prozentualer Internetzugang\", \"CO2\" FROM public.\"InternetJahre\", public.\"chosen\", public.\"Emissionen\" WHERE \"InternetJahre\".\"Place\" = \"chosen\".\"countries\" AND \"chosen\".\"years\" = \"InternetJahre\".\"Time\" AND \"Emissionen\".\"Land\" = \"chosen\".\"countries\" AND \"Emissionen\".\"Jahr\" = \"chosen\".\"years\" ", c)
	fig, axs = plt.subplots(2)
	df.plot(ax = axs[0], kind = "bar", x = "RES" , y="Prozentualer Internetzugang")
	df.plot(ax = axs[1], kind = "bar", x = "RES", y="CO2")
	plt.show()
	
	c.close()
	
	
def queries():
	
	cont = "J"
	while cont == "J":
		visualize()
		cont = input("Erneut Starten? [J/N]")

queries()
		
