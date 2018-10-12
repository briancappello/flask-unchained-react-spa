#!/bin/sh

sphinx-autobuild . _build/html --re-ignore ".+___jb_\w+___$"
