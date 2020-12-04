package com.ochronus
package year2020

object PassportValidator {

  def checkRequiredFields(fields: Map[String, String]): Boolean = Seq("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid").intersect(fields.keys.toSeq).size == 7

  def byr(fields: Map[String, String]) = validateYear(fields("byr"), 1920, 2002)
  def iyr(fields: Map[String, String]) = validateYear(fields("iyr"), 2010, 2020)
  def eyr(fields: Map[String, String]) = validateYear(fields("eyr"), 2020, 2030)

  def hgt(fields: Map[String, String]) = {
    val cm = """(\d+)cm""".r
    val inch = """(\d+)in""".r
    fields("hgt") match {
      case cm(height) => height.toInt>= 150 && height.toInt <= 193
      case inch(height) => height.toInt>= 59 && height.toInt <= 76
      case _ => false
    }
  }

  def hcl(fields: Map[String, String]) = fields("hcl").matches("""#([0-9a-f]{6})""")
  def ecl(fields: Map[String, String]) = Seq("amb", "blu", "brn", "gry", "grn", "hzl", "oth").contains(fields("ecl"))
  def pid(fields: Map[String, String]) = fields("pid").matches("""(\d{9})""")

  private def validateYear(year: String, min: Int, max: Int) = year.toInt >= min && year.toInt <= max

}
