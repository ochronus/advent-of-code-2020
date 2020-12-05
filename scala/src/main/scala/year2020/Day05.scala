package com.ochronus
package year2020

import utils.File

class Day05 {
  private val passportIDs = File.readFileLines("day05.input.txt").map { l =>
    l
      .replaceAll("F|L", "0")
      .replaceAll("B|R", "1")
  }.map(Integer.parseInt(_, 2))

  def part1(): Long = {
    passportIDs.max
  }

  def part2(): Long = {
    passportIDs
      .sorted
      .sliding(2)
      .collectFirst { case List(a, b) if a + 1 != b => a + 1 }
      .get
  }
}
