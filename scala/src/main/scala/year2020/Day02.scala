package com.ochronus.year2020

import com.ochronus.utils.File

class InputLine(var low: Int, var high: Int, var char: Char, var password: String) {
  def part1: Boolean = {
    val count = password.count(_ == char)
    count >= low && count <= high
  }

  def part2: Boolean = {
    (password(low - 1)) == char ^ (password(high - 1) == char)
  }

}

class Day02 {
  private val lineRegexp = """(\d+)-(\d+) (\w): (\w+)""".r

  private val lines = File.readFileLines("day02.input.txt").map {
      case lineRegexp(low, high, char, password) => new InputLine(low.toInt, high.toInt, char.head, password)
  }

  def part1(): Int = lines.count(_.part1)

  def part2(): Int = lines.count(_.part2)
}
