This repository contains code and data for the manuscript "Evaluating the use of ABBA-BABA statistics to locate introgressed loci" by Simon H. Martin (<shm45@cam.ac.uk>), John W. Davey (<jd626@cam.ac.uk>) and Chris D. Jiggins, available on [bioRxiv](http://biorxiv.org) ([doi: 10.1101/001347](http://biorxiv.org/content/early/2013/12/11/001347)).

The results in the paper were generated as follows. If details are missing or incorrect, please tell us.

# Figures

Figures were generated using the following scripts, all of which have data files hard coded and so will need modifying for new data sets. `compare_f_estimators.r` performs simulations and generates Figure 2 and Figure S1.
```
./Figure_1.R
./compare_f_estimators.r
./Figures_3_S2_S3.R
./Figure_4.R
./Figure_5.R
./Table_S1.R
```

# Simulations

The model scripts should be general enough to be used for your own models. If they are not, please let us know. They require the R packages [phyclust](http://cran.r-project.org/web/packages/phyclust/index.html), [plyr](http://plyr.had.co.nz), [yaml](http://cran.r-project.org/web/packages/yaml/index.html), [optparse](http://cran.r-project.org/web/packages/optparse/index.html), [ggplot2](http://ggplot2.org), [gridExtra](http://cran.r-project.org/web/packages/gridExtra/index.html), [reshape](http://had.co.nz/reshape/) and [stringr](http://cran.r-project.org/web/packages/stringr/index.html), and for [Seq-Gen](http://beast.bio.ed.ac.uk/software/seqgen/) to be installed and in your path.

Models can be generated using the `shared_ancestry_simulator.R` script. A single combined model can be generated like this:
```
./shared_ancestry_simulator.R -w 10000 -t 60 -c Alternate_t123-0.4_t23-0.2.yml:0.1,Background_t123-0.6_t21-0.4.yml:0.9
```

This will generate 10000 windows, 10% of which will be generated using the model described in the file `Alternate_t123-0.4_t23-0.2.yml` and 90% of which will be generated using `Background_t123-0.6_t21-0.4.yml`, using 60 threads. See the model files folders for the YAML files generated for this paper. The CSV files for the models will be made available in a Data Dryad repository on publication and can be made available on request.

A single model, as used for the null models reported in the paper, can be run like this:
```
./shared_ancestry_simulator.R -w 10000 -t 60 -c Background_t123-0.6_t21-0.4.yml:1
```


The model YAML files were generated by the `run_model_combinations.py` script, using the following commands:
```
./run_model_combinations.py -m Model_parameter_list.csv -w 10000 -t 30 -s 0.01 -l 5000 -r 5
./run_model_combinations.py -m Model_parameter_list.csv -w 10000 -t 30 -s 0.01 -l 5000 -r 50
```

Option `-m` specifies a file containing the list of models to simulate (available in the repository). Option `-w` specifies the number of windows and `-t` the number of threads. For Seq-Gen options, `-s` defines the scale factor and `-l` the length of sequence. `-r` defines the recombination rate for ms.

ms produces a tree with branch lengths and a set of variant sites. This set of variant sites is generated assuming an infinite sites model. We produce output using this set of variant sites (in files with '.ms.' in the name) but also generate sequences from the ms tree using Seq-Gen (in files with '.sg.' in the name), which does not assume an infinite sites model. We used the Seq-Gen output for all analyses in the paper.

Summary statistics for the models found in the `partition.summary` and `dxy.summary` files were generated as follows:

```
./generate_summary_statistics.R -m model_files_win10000_s0.01_l5000_r5 -l Model_parameter_list.csv -t 10
./generate_summary_statistics.R -m model_files_win10000_s0.01_l5000_r50 -l Model_parameter_list.csv -t 10
```

Summary files are produced for alternate and null models and for ms and Seq-Gen output. The Seq-Gen files used for the paper analyses are included in the repository.


# Real Heliconius data

Real data for the Heliconius genome, split into 5 kb windows, can be found in the files `Heliconius_autosome_windows.csv` and `Heliconius_Zchromosome_windows.csv`.

Calculation of summary statistics was done with the python script `egglib_sliding_windows.py`, which makes use of the EGGLIB library. Input was a "calls" format file, provided in [Martin et al. 2013](http://dx.doi.org/10.1101/gr.159426.113). Window size is specified with the `-w` flag, sliding increment with the `-i` flag and minimum number of sites with the `-m` flag. The latter is a hard cutoff, and windows with fewer sites are discarded. There is also a soft cutoff between 0 and 1, specified with `--minimumExploitableData`. The script will output a column called sitesOverMinExD. At a value of 0.5, this would report the number of sites in the window that had genotype calls for at least 50% of the individuals. To analyse autosomes and Z-linked scaffolds separately, the `--include` and `--exclude` flags were used, along with the file `Hmel1-1_Zupdated_Zscafs.txt`, which provides names of all Z-linked scaffolds provided in [Martin et al. 2013](http://dx.doi.org/10.1101/gr.159426.113). For the Z chromosome analysis, ploidy was specified using the `--ploidy` flag, because there were two females in the dataset of [Martin et al. 2013](http://dx.doi.org/10.1101/gr.159426.113). See the commands below.


Commands to calculate values for the whole genome were, for autosomes:

```
python egglib_sliding_windows.py -i set31.Zupdated.union.geno -o set31.Zupdated.union.autoScafs.PiDxyABBAs.w5m1s5.csv -w 5000 -m 1000 -s 5000 --report 100 -a pi,dxy,ABBABABA,popS,S -p "P1[ag108,ag572,ag112,ag569];P2[am216,am160,am48,am293];P3[tiP86,tiP313,tiP84,tiP57];O[hec273,eth67,ser202,par371];P3a[tiP86,tiP313];P3b[tiP84,tiP57]"  --minimumExploitableData 0.5 --exclude Hmel1-1_Zupdated_Zscafs.txt
```

And for the Z chromosome:
```
python egglib_sliding_windows.py -i set31.Zupdated.union.geno -o set31.Zupdated.union.chrZscafs.PiDxyABBAs.w5m1s5.csv -w 5000 -m 1000 -s 5000 --report 100 -a pi,dxy,ABBABABA,popS,S -p "P1[ag108,ag572,ag112,ag569];P2[am216,am160,am48,am293];P3[tiP86,tiP313,tiP84,tiP57];O[hec273,eth67,ser202,par371];P3a[tiP86,tiP313];P3b[tiP84,tiP57]"  --minimumExploitableData 0.5 --include Hmel1-1_Zupdated_Zscafs.txt --ploidy "2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2"
```


[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/a5cff0af4f8cf280f6954c7dcd702477 "githalytics.com")](http://githalytics.com/johnomics/Martin_Davey_Jiggins_evaluating_introgression_statistics)