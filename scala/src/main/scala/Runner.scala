package com.ochronus

import year2020.{Day01, Day02}

object Runner {
  def main(args: Array[String]) = {
    val problem1 = new Day01()
    println("Day 1 part 1: " + problem1.part1())
    println("Day 1 part 2: " + problem1.part2())

    val problem2 = new Day02()
    println("Day 2 part 1: " + problem2.part1())
    println("Day 2 part 2: " + problem2.part2())
  }
}