open System
open System.IO
open System.Text.RegularExpressions

type PwLine = { MinOccurences: int; MaxOccurences: int; Character: char; Password: String; }

let (|ParseRegex|_|) regex str =
   let m = Regex(regex).Match(str)
   if m.Success
   then Some (List.tail [ for x in m.Groups -> x.Value ])
   else None


let parseLine str =
   match str with
     | ParseRegex "(\d+)-(\d+) (\w+): (\w+)" [min; max; char; password]
          -> { MinOccurences = int min; MaxOccurences = int max; Character = char.[0] ; Password = password; }

let validate1 pwline = 
    let occurences = 
        pwline.Password
            |> Seq.filter (fun x' -> x' = pwline.Character)
            |> Seq.length
    occurences <= pwline.MaxOccurences && occurences >= pwline.MinOccurences

let validate2 pwline = 
    (pwline.Password.[pwline.MinOccurences - 1] = pwline.Character) <> (pwline.Password.[pwline.MaxOccurences - 1] = pwline.Character)


[<EntryPoint>]
let main argv =
    let lines = File.ReadLines("input.txt")                
    let linesList =
        lines
            |> Seq.map parseLine
            |> List.ofSeq
    
    let part1 = 
        linesList
            |> Seq.filter validate1
            |> List.ofSeq

    let part2 = 
        linesList
            |> Seq.filter validate2
            |> List.ofSeq

    printfn "%d" part1.Length
    printfn "%d" part2.Length

    0