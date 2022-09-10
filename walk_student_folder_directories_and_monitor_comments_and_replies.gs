/////////////////////////////////////////////////////////////

function collate_comments(folder_id, comment_tracker, student=null)
{
  let this_folder = DriveApp.getFolderById(folder_id) 
  let subfolders = this_folder.getFolders()

  if (student === null) { student = this_folder.getEditors()[0].getEmail()}

  if (comment_tracker === undefined) { comment_tracker = [] }

  while (subfolders.hasNext())
  {
    base = false;
    comment_tracker = collate_comments(subfolders.next().getId(), comment_tracker, student)
  }

  let files = this_folder.getFiles()

  Logger.log("Getting files of folder", this_folder.getName())
  while (files.hasNext())
  {
    let f = files.next()
    let id = f.getId()
    let this_file = new Array(MAX_COMMENTS).fill('') // because .setValues() does not accept irregular shaped arrays
    this_file[0] = student
    this_file[1] = f.getName();
    this_file[2] = f.getUrl();

    let y = 3;

    //Logger.log(f.getName())
    let comment_access = true;
    let comment_set = [];
    try
    {
      comment_set = Drive.Comments.list(id)['items']
    }
    catch (e)
    {
      comment_access = false;
    }


    if (comment_access && (comment_set.length > 0))
    {
      for (let this_comment of comment_set)
      {
        let comment_log = this_comment.author.displayName + ": " + this_comment.content
        this_file[y] = comment_log;
        y++;

        //Logger.log("has " + this_comment.replies.length.toString() + " replies")

        for (let this_reply of this_comment.replies)
        {
          comment_log = this_reply.author.displayName + ": " + this_reply.content
          //Logger.log(comment_log)
          this_file[y] = comment_log;
          y++;
        }
      }
    }

    comment_tracker.push(this_file)

  }

  return comment_tracker
}

/////////////////////////////////////////////////////////////

function get_all_comments(folder_id)
{
  let comment_tracker = collate_comments(folder_id)
  let ss = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("comment_tracker")
  Logger.log(comment_tracker)
  ss.getRange(1, 2, comment_tracker.length, comment_tracker[0].length).setValues(comment_tracker)
}

/////////////////////////////////////////////////////////////