package com.ochronus.utils

import scala.io.Source

object File {

  /**
   * Read the contents of a resource file given its relative path into a sequence of lines
   */
  def readFileLines(filename: String): Seq[String] =
    Source.fromFile(filename).getLines().toSeq

  def readFileString(filename: String): String =
    Source.fromFile(filename).mkString
}
