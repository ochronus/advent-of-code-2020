package com.ochronus
package year2020

import scala.collection.Searching._
import utils.File

class Day09 {
  private val numbers = File.readFileLines("day09.input.txt").map(_.toLong)
  val windowSize = 25

  def part1(): Long = {
      numbers.drop(windowSize).zip(numbers.sliding(windowSize)).find(elem => elem._2.combinations(2).forall(_.sum != elem._1)).get._1
  }

  def part2(outlier: Long): Long = {
    for (i <- 0 to numbers.length - 1) {
      for (j <- i + 2 to numbers.length - 1) {
        val slice = numbers.drop(i).take(j - i)
        if (slice.sum == outlier) return (slice.min + slice.max)
      }
    }
    0
  }
}
