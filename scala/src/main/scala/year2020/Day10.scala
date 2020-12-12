package com.ochronus
package year2020

import utils.File

class Day10 {
  private val myBag = File.readFileLines("day10.input.txt").map(_.toLong)
  private val adapters:Seq[Long] = 0L +: myBag.sorted :+ (myBag.max + 3)

  private val joltDiffs = adapters.sliding(2).toList.map{case List(a, b) => b - a}

  def part1(): Long = joltDiffs.count(_ == 1) * joltDiffs.count(_ == 3)
  
  def part2(): Long = ???

}
