package com.ochronus
package year2020

import utils.File

class Day03 {
  private val lines = File.readFileLines("day03.input.txt")
  private val (width, height) = (lines.head.size, lines.size)
  private val travelPatterns = Seq((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

  def part1(): Long = {
    travelAndCount(3, 1)
  }

  def part2(): Long = {
    travelPatterns.map(pattern => travelAndCount(pattern._1, pattern._2)).product
  }

  def travelAndCount(right: Int, down: Int): Long = {
    val stepsDown = (height.toFloat / down).ceil.toInt
    (0 until stepsDown).count(i => lines(i * down)((right * i) % width) == '#').toLong
  }
}
