# Makefile for source rpm: mono
# $Id$
NAME := mono
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
