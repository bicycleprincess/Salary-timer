// read time
import Foundation
import Cocoa

let currentTime = Foundation.NSDate()
//print(currentTime)

let dateFormatter = Foundation.DateFormatter()
//dateFormatter.dateFormat = "yyyy-MM-dd HH:mm:ss"§

let currentTimeInSecond = NSDate().timeIntervalSince1970
//print(currentTimeInSecond)

let string_current_time = Date(timeIntervalSince1970: currentTimeInSecond)
//print(string_current_time)


// read file

// first try
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

// second try
let fileManager = FileManager.default
let txtPath = "/Users/yangwei/env/Swift/iphone_app/Sources/log.txt"
let url = URL(fileURLWithPath: txtPath)
//let content = try String(contentsOfFile: txtPath)
//print(content)

// write file
//var dataToWrite = "My Interesting Data: "  + time_now
var dataToWrite = "My Interesting Data: \(currentTimeInSecond)"
print(dataToWrite)
let data = Data(dataToWrite.utf8)
try! dataToWrite.write(to: url, atomically: true, encoding: String.Encoding.utf8)
