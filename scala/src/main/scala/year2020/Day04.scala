package com.ochronus
package year2020

import utils.File
import com.ochronus.year2020.PassportValidator

class Day04 {
  private val rawPassports = File.readFileString("day04.input.txt").split("\n\n")
  private val passports = rawPassports.map(parseRawPassport)
  private val passPortsWithRequiredFields = passports.filter(PassportValidator.checkRequiredFields)

  private def parseRawPassport(str: String) : Map[String, String] = {
    str.split("[ \n]")
      .map(_.split(":"))
      .map(p => p(0) -> p(1)).toMap
  }


  def part1(): Long = {
    passPortsWithRequiredFields.size
  }

  def part2(): Long = {
    passPortsWithRequiredFields
      .filter(PassportValidator.byr)
      .filter(PassportValidator.iyr)
      .filter(PassportValidator.eyr)
      .filter(PassportValidator.hgt)
      .filter(PassportValidator.hcl)
      .filter(PassportValidator.ecl)
      .filter(PassportValidator.pid)
      .size
  }


}
