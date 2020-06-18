import Foundation
import Cocoa

let month = [1,3,5,7,8,10,12]

let currentTime = Foundation.NSDate()
//print(currentTime)

let dateFormatter = Foundation.DateFormatter()
dateFormatter.dateFormat = "yyyy-MM"

//get the year and month
var today = dateFormatter.string(from:currentTime as Date)
var current_year = Int(today.prefix(4))
var current_month = Int(today.suffix(2))
//print(current_year as Any, current_month as Any)
var days = Int()


// find the days of month --> so ugly.... :-/
if current_month == 2 {
	if ((current_year! % 4 == 0) && (current_year! % 100 != 0) || (current_year! % 400 == 0)) {
		days = 29
	}else {
		days = 28
	}
}else {
	if month.contains(where:{$0==current_month}) {
		days = 31
	}else {
		days = 30
	}
}
//print(days)

// time for compairsion and saving
let currentTimeInSecond = NSDate().timeIntervalSince1970
//print(currentTimeInSecond)

//let string_current_time = Date(timeIntervalSince1970: currentTimeInSecond)
//print(string_current_time)

let fileManager = FileManager.default
let txtPath = "/Users/yangwei/env/Swift/iphone_app/Sources/log.txt"
let url = URL(fileURLWithPath: txtPath)
//print(url.absoluteURL)

// read file
let text = try String(contentsOf: url, encoding: .utf8)
//let index = text.index(text.firstIndex(of: ":")!,offsetBy:1)// ?? text.endIndex
//let index = text.index(text.firstIndex(of: ":")!,offsetBy:0)// ?? text.endIndex
//print(text[text.index(after:index)...])
//let saved_time = Double(text[text.index(after:index)...])
//print(saved_time!)

var salary:Double = 3550
print(salary)


print(text.split(separator:":"))
let saved_data = text.split(separator:":")
let saved_year = Int(saved_data[0].prefix(4))
let saved_month = Int(saved_data[0].suffix(2))
let saved_time = Double(saved_data[1])
let saved_base = Double(saved_data[2])
let saved_working_hour = Int(saved_data[3])
print(saved_year as Any, saved_month as Any, saved_time as Any)

if current_month != saved_month{
	// TODO
	// func updateBase()
	print("any changes about your salary?")
}


//if currentTimeInSecond !== saved_time {

//}

// write data into file


var dataToWrite = "\(today):\(currentTimeInSecond):\(salary):\(40)"
//print(dataToWrite)
let data = Data(dataToWrite.utf8)
try! dataToWrite.write(to: url, atomically: true, encoding: String.Encoding.utf8)


/*
if let filepath = Bundle.main.path(forResource: "log", ofType: "txt") {
    do {
        let contents = try String(contentsOfFile: filepath)
        print(contents)
    } catch {
        print("contents could not be loaded")
    }
} else {
    print("log.txt not found!")
}
*/