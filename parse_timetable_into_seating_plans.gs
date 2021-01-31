done = []
ss = SpreadsheetApp.getActiveSpreadsheet()

function del() {
  var sheets = ss.getSheets()
  for (var i in sheets)
  {
    if (i > 5)
    {
      ss.deleteSheet(sheets[i])
    }
  }
}

function parse_timetable() {

  var HEADERS = 'PK	Session	Exam Date	Exam Day	Start Time	Syllabus	Code	Lookup Code	Component Title	Venue	Duration	End Time	Duration w/ Extra Time	End Time w/ Extra Time	Count	Students Involved	Exam Board	ET count	ETR	SR Counts	SR 1	SR 2	SR 3	SD305 (Overspill)	SR needed	EHB count	Exam Hall Candidates	Overspill room		FR Count	EH Laptops	SD317 /SD308 Laptops		SD404 Laptops	SD402 Laptops	SD421 Laptops				Exam Hall FLAG	Overspill FLAG	Extra time FLAG	SR 1 FLAG	SR 2 FLAG	sheet_name'.split('\t')


  
  var data = ss.getSheetByName("exam_data").getRange("A2:AS66").getValues()




  

  for (var i = 0; i< data.length; i++)
  {
    
    var row = data[i]

    var pk = row[0]

    var code = row[HEADERS.indexOf("Code")]
    var eh =   row[HEADERS.indexOf("Exam Hall FLAG")]
    var os =   row[HEADERS.indexOf("Overspill FLAG")]
    var et =   row[HEADERS.indexOf("Extra time FLAG")]
    var sr1 =  row[HEADERS.indexOf("SR 1 FLAG")]
    var sr2 =  row[HEADERS.indexOf("SR 2 FLAG")]

    var sheet_name = row[HEADERS.indexOf("sheet_name")]




    if (eh) {    copy_seating_plan(sheet_name + " - [EH]", "exam_hall", pk, code)}
    if (os) {    copy_seating_plan(sheet_name + " - [OS]","os_room", pk, code)}
    if (et) {    copy_seating_plan(sheet_name + " - [ET]","extra_time_room", pk, code)}  
    if (sr1) {    copy_seating_plan(sheet_name + " - [SR1]", "sr_1", pk, code)}
    if (sr2) {    copy_seating_plan(sheet_name + " - [SR2]","sr_2", pk, code)}
      

  }


  

}


function copy_seating_plan(name, template, pk, code)
{

  var duplicate = false;
    for (var j in done)
    {
     if (done[j].indexOf(name) > -1)
     {
        duplicate = true;
        break;
     }
    }

     if (duplicate) { return } else { done.push(name)}

    var sheet = ss.getSheetByName(template).copyTo(ss).setName(name + " " + code + " etc.")

    sheet.getRange("P1").setValue(pk)

}