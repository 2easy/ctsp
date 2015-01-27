#! /bin/sh

# Usage: ./generate_graph.sh path/to/input result

# where input is filename without csv extension

# Script generates graph in /path/to/input.png



# echo $1

/usr/bin/gnuplot <<- EOF

  set term png

  set output "${1}image.png"

  set logscale y 10

  plot "tabooresults" with linespoints title 'SSwTaboo', "annealingresults" with linespoints title 'SimulatedAnnealing' ,"antresults" with linespoints title 'Ants'

EOF




