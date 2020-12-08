package com.ochronus
package year2020

import utils.File

class Day08 {
  private val originalProgram = File.readFileLines("day08.input.txt").map(line => (line.split(' ')(0), line.split(' ')(1).toInt))

  def execute(ip: Int = 0, acc: Int = 0, alreadyExecuted: Set[Int] = Set.empty)
             (implicit program: Seq[(String, Int)]): (Int, Boolean) = {

    if (ip == program.size) {
      (acc, true)
    }
    else if (alreadyExecuted.contains(ip)) {
      (acc, false)
    } else {
      program(ip) match {
        case ("acc", value) => execute(ip + 1, acc + value, alreadyExecuted + ip)
        case ("jmp", value) => execute(ip + value, acc, alreadyExecuted + ip)
        case ("nop", _) => execute(ip + 1, acc, alreadyExecuted + ip)
      }
    }
  }

  def part1(): Long = {
    val res = execute()(originalProgram)
    res._1
  }

  def part2(): Option[Long] = {
    for ((instruction, ip) <- originalProgram.zipWithIndex) {
      val newInstruction = instruction match {
        case ("jmp", value) => ("nop", value)
        case ("nop", value) => if (value != 0) ("jmp", value) else ("nop", value)
        case ("acc", value) => ("acc", value)
      }
      if (newInstruction != instruction) execute()(originalProgram.updated(ip, newInstruction)) match {
        case (acc, true) => return Some(acc)
        case _ => None
      }
    }
    None
  }
}
