import csv

print("Starting Processing...")

with open("team-data.csv", 'r', newline='') as datafile:
	data_reader = csv.DictReader(datafile)
	
	with open("src/index.html", "w") as htmlfile:
		
		print("Write Header and Style")
		
		htmlfile.write("""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FSGP 2025 Teams</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
  </head>
  <body>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
.accordion-button::after {
  transition: transform 0.2s ease-in-out;
}
.accordion-button.collapsed::after {
  transform: rotate(0deg);
}
.accordion-button:not(.collapsed)::after {
  transform: rotate(180deg);
}
.accordion-button::after {
  font-size: 1.5rem;
}
.accordion-button {
  transition: background-color 0.3s ease;
}
.accordion-button:hover {
  background-color: #f1f1f1;
}
</style>""")
		
		print("Staring Accordion")
		
		htmlfile.write("""<div class="accordion mx-auto px-2" style="max-width: 98%;" id="solarTeamAccordion">""")
		
		firstRun=True
		for team in data_reader:
			print(f"""Processing: {team['Team Name']}""")
			
			identifier = team['Team Name'].replace(" ", "-")
			
			htmlfile.write(f"""<div class="accordion-item">
    <h2 class="accordion-header" id="heading-{identifier}">
      <button class="accordion-button {"" if firstRun else "collapsed"} d-flex flex-column flex-md-row align-items-start align-items-md-center gap-2" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{identifier}" aria-expanded="{"true" if firstRun else "false"}" aria-controls="collapse-{identifier}" style="cursor: pointer;">
        <div class="row w-100">
          <div class="col-md-6">
            <img class="img-fluid team-photo" src="./img/{team['Number']}.jpg" alt="{team['Team Name']} Team Photo" />
          </div>
          <div class="col-md-6">
            <h3 class="mb-1 fw-bold">#{team['Number']} - {team['Car Name']}</h3>
            <div class="d-flex align-items-center mb-2">""")
			if team['Class'] == "SOV":
				htmlfile.write("""              <img src="https://www.americansolarchallenge.org/ASC/wp-content/uploads/2022/06/person-icon.png" style="height: 1.5em;" alt="SOV Class" />""")
			else:
				htmlfile.write("""              <img src="https://www.americansolarchallenge.org/ASC/wp-content/uploads/2022/06/multi-person-icon.png" style="height: 1.5em;" alt="SOV Class" />""")
			
			if team['Country'] == "USA":
				htmlfile.write("""              <span class="ms-2 fs-3"><img src="https://flagcdn.com/us.svg" width="24" alt="US Flag" class="me-2" /></span>""")
			elif team['Country'] == "CANADA":
				htmlfile.write("""              <span class="ms-2 fs-3">  <img src="https://flagcdn.com/ca.svg" width="24" alt="Canada Flag" class="me-2" /></span>""")
			elif team['Country'] == "Puerto Rico":
				htmlfile.write("""              <span class="ms-2 fs-3"><img src="https://flagcdn.com/pr.svg" width="24" alt="Puerto Rico Flag" class="me-2" /></span>""")
			htmlfile.write("""            </div>""")
			
			htmlfile.write(f"""            <h4 class="mb-0">{team['Team Name']}</h4>
            <p class="text-muted mb-1">{team['School Name']}</p>
            <div class="fs-5 mb-2">""")
			if team['Class'] == "SOV":
				htmlfile.write(f"""             <span>{team['Weight']}kg</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<span>{team['Dimensions']}</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<span>{team['Wheels']} wheels</span>""")
			else:
				htmlfile.write(f"""             <span>{team['Weight']}kg</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<span>{team['Dimensions']}</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<span>{team['Passengers']} Passengers</span>""")
            
			htmlfile.write(f"""
            </div>
            <div class="fs-5 mb-2">{team['Solar Power']}W {team['Solar Manu']} {team['Solar Chemistry']} array</div>
            <div class="fs-5 mb-2">{team['Battery Power']}kWh {team['Battery Manu']} {team['Battery Chemistry']} battery</div>""")
			
			htmlfile.write("""            <div class="mt-2">""")
			
			if team['Website']:
				htmlfile.write(f"""            <a href="{team['Website']}" target="_blank" class="text-dark me-2"><i class="fas fa-globe fa-lg"></i></a>""")
			if team['Facebook']:
				htmlfile.write(f"""            <a href="{team['Facebook']}" target="_blank" class="text-dark me-2"><i class="fab fa-facebook fa-lg"></i></a>""")
			if team['Instagram']:
				htmlfile.write(f"""            <a href="{team['Instagram']}" target="_blank" class="text-dark me-2"><i class="fab fa-instagram fa-lg"></i></a>""")
			if team['Linkedin']:
				htmlfile.write(f"""            <a href="{team['Linkedin']}" target="_blank" class="text-dark me-2"><i class="fab fa-linkedin fa-lg"></i></a>""")
			
			htmlfile.write("""            </div>
          </div>
        </div>
      </button>
    </h2>""")
			
			htmlfile.write(f"""    <div id="collapse-{identifier}" class="accordion-collapse collapse {"show" if firstRun else ""}" aria-labelledby="heading-{identifier}" data-bs-parent="#solarTeamAccordion">
      <div class="accordion-body">
        <p>{team['Bio']}</p>
        <hr>""")
			
			htmlfile.write(f"""        <h5>{team['Car Name']} Specifications</h5>
        <i>Specifications are provided by the team</i><br><br>
        <table class="table table-sm">
          <tr><th class="text-end">Size</th><td>{team['Weight']}kg | {team['Dimensions']}</td></tr>
          <tr><th class="text-end">Solar Array</th><td>{team['Solar Power']}W {team['Solar Manu']} {team['Solar Chemistry']}</td></tr>
          <tr><th class="text-end">Battery</th><td>{team['Battery Power']}Wh {team['Battery Manu']} {team['Battery Chemistry']} ({team['Battery Weight']}kg)</td></tr>
          <tr><th class="text-end">Motor</th><td>{team['Motor Number']}x {team['Motor Power']}kW {team['Motor Manu']} {team['Motor Type']}</td></tr>
          <tr><th class="text-end">Wheels</th><td>{team['Wheels']}x {team['Wheel Manu']} {team['Wheel Material']}</td></tr>
          <tr><th class="text-end">Tires</th><td>{team['Tire Size']} {team['Tires']}</td></tr>
          <tr><th class="text-end">Chassis</th><td>{team['Chassis']}</td></tr>
        </table>
      </div>
    </div>
  </div>""")
			
			firstRun = False

		print("Ending Accordion, Adding Footer")
		
		htmlfile.write("""</div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
  </body>
</html>""")
		
		print("Complete")