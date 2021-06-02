all_files = []
TAG_SAG_ROOT = "0AE4t_R8ie1nYUk9PVA"

function walk_folders(folder)
{

  Logger.log("walking " + folder.getName())
  var sub_folders = folder.getFolders()

  while (sub_folders.hasNext())
  {
    walk_folders(sub_folders.next())
  }

  var files = folder.getFiles()

  while (files.hasNext())
  {
    var f = files.next()
    var parent = f.getParents().next()
    all_files.push([f.getName(), f.getUrl(), parent.getName()])
  }

}


function log_files()
{

  walk_folders(DriveApp.getFolderById(TAG_SAG_ROOT))
  var ss = SpreadsheetApp.openById("1A4pTpZJGFDIvMD1vkKuzFQTTEc8QljQJjEVVMQUEdO8")
  var sheet = ss.setActiveSheet(ss.getSheetByName("find_files"))
  var r = sheet.setActiveRange(sheet.getRange("A1:C"+all_files.length))
  r.setValues(all_files) 

}