// read time
import Foundation
import Cocoa

let currentTime = Foundation.NSDate()
//print(currentTime)

let dateFormatter = Foundation.DateFormatter()
dateFormatter.dateFormat = "yyyy-MM"

//get the year and month
var today = dateFormatter.string(from:currentTime as Date)
var year = Int(today.prefix(4))
var month = Int(today.suffix(2))
print(year as Any, month as Any)

let currentTimeInSecond = NSDate().timeIntervalSince1970
//print(currentTimeInSecond)


//let string_current_time = Date(timeIntervalSince1970: currentTimeInSecond)
//print(string_current_time)


let fileManager = FileManager.default
let txtPath = "/Users/yangwei/env/Swift/iphone_app/Sources/log.txt"
let url = URL(fileURLWithPath: txtPath)

var dataToWrite = "\(today): \(currentTimeInSecond)"
//print(dataToWrite)
let data = Data(dataToWrite.utf8)
try! dataToWrite.write(to: url, atomically: true, encoding: String.Encoding.utf8)

//let month = [1,3,5,7,8,10,12]

// read file
let text = try String(contentsOf: url, encoding: .utf8)
let index = text.index(text.firstIndex(of: ":")!,offsetBy:1)// ?? text.endIndex
print(text[text.index(after:index)...])

let saved_time = Double(text[text.index(after:index)...])
print(saved_time!)

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