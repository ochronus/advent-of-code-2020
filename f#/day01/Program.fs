open System
open System.IO


let Part1 (x: int list) : int =
    let result = [ for n1 in x do
                   for n2 in x do
                   if n1 + n2 = 2020 then n1 * n2 ]
    result.Head

let Part2 (x: int list) : int =
    let result = [ for n1 in x do
                   for n2 in x do
                   for n3 in x do
                   if n1 + n2 + n3 = 2020 then n1 * n2 * n3 ]
    result.Head

[<EntryPoint>]
let main argv =
    let lines = File.ReadLines("input.txt")                
    let intList = lines |> Seq.map int |> List.ofSeq

    printfn "%d" (Part1 intList)
    printfn "%d" (Part2 intList)

    0