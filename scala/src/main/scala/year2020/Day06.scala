package com.ochronus
package year2020

import utils.File


class Day06 {
  private val groups = File.readFileString("day06.input.txt").split("\n\n").map(_.linesIterator.toSeq)

  def part1(): Long = groups.map(_.reduce(_ ++ _).toSet.size).sum

  def part2(): Long = groups.map(group => group.map(_.toSet).reduce(_ & _).size).sum
}
