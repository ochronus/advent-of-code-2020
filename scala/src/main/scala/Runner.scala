package com.ochronus

import year2020.{Day09}

object Runner {
  def main(args: Array[String]) = {
    val problem = new Day09()
    val outlier = problem.part1()
    println("part 1: " + outlier)
    println("part 2: " + problem.part2(outlier))
  }
}