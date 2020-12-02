package com.ochronus.year2020

import scala.util.Try
import com.ochronus.utils.File

class Day01 {
  private val numbers = File.readFileLines("day01.input.txt").flatMap(row => Try(row.toInt).toOption)

  def part1(): Int = {
    for (i <- numbers; j <- numbers) {
      if (i + j == 2020)
        return i * j
    }

    -1
  }

  def part2(): Int = {
    for (i <- numbers; j <- numbers; k <- numbers) {
      if (i + j + k == 2020)
        return i * j * k
    }

    -1
  }
}
