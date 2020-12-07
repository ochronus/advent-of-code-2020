package com.ochronus
package year2020

import utils.File

class Day07 {
  private val ruleRegexp = """(.*) bags contain (.*)""".r
  private val containsRegexp = """\s*(?:(\d+)\s+(\w+\s\w+)\s(?:bag|bags)[,.])""".r
  private val rules = File.readFileLines("day07.input.txt").map(parseRule).toMap
  private val ShinyGold = "shiny gold"

  def parseRule(s: String): (String, List[(String, Int)]) = {
    val ruleRegexp(bag, containsList) = s
    val contents = containsRegexp.findAllMatchIn(containsList).map(m => (m.group(2), m.group(1).toInt)).toList
    bag.trim -> contents
  }

  def part1(): Long =
    rules.keys.toList
      .map(checkIfCanContain(_, ShinyGold))
      .count(identity)

  def checkIfCanContain(bag: String, searchedColor: String): Boolean = {
    def helper(bags: List[(String, Int)]): Boolean = {
      bags match {
        case Nil => false
        case (color, _) :: _ if color == searchedColor => true
        case (color, _) :: t => helper(rules(color)) || helper(t)
      }
    }

    helper(rules(bag))
  }

  def part2(): Long = bagCost(ShinyGold)

  def bagCost(bag: String): Int = {
    def helper(bags: List[(String, Int)]): Int =
      bags match {
        case Nil => 0
        case (color, count) :: t => (count + count * helper(rules(color))) + helper(t)
      }

    helper(rules(bag))
  }
}
