


.. _installation_software:

Installation
============

Python
------
|software| is now being developed in Python 3.6.9 but should be compatible with Python2.
If you experience problems with your version of Python and |software| please contact |myemail| or
post an issue on the project homepage at

   * http://github.com/hklarner/PyBoolNet/issues


Linux
-----

Download the latest release from

   * http://github.com/hklarner/PyBoolNet/releases

We recommend to install the package using *pip*. If it is not already installed on your computer try::

   $ sudo apt install python-pip

Make sure that :ref:`NetworkX <installation_networkx>`, :ref:`Graphviz <installation_graphviz>` and :ref:`ImageMagick <installation_imagemagick>` are installed::

   $ sudo pip3 install networkx
   $ sudo apt install graphviz
   $ sudo apt install imagemagick

Install |software| with *pip*::

   $ sudo pip3 install git+https://github.com/hklarner/PyBoolNet@2.31.0

which should place the package here::

   /usr/local/lib/python<version>/dist-packages/PyBoolNet

Use the option ``--user`` (literally) if you do not have sudo rights::

   $ pip3 install git+https://github.com/hklarner/PyBoolNet@2.31.0 --user

The package is likely going to be placed here::

   /home/<user>/.local/lib/python<version>/dist-packages/PyBoolNet

where ``<user>`` is the name you are logged in with (``$ whoami``) and ``<version>`` is the Python version you are using.

You should now be able to import |software|::

   $ python
   >>> import PyBoolNet


To remove |software| using *pip* run::

      $ pip3 uninstall PyBoolNet

If you do not have *pip*, all files must be removed manually.


Mac OS
------
Download the latest release from

   * http://github.com/hklarner/PyBoolNet/releases

We recommend to install the package using *pip*. If it is not already installed on your computer try::

   $ sudo easy_install pip

or if you do not have super user rights::

   $ easy_install --user pip

Install NetworkX_ with::

   $ sudo pip3 install networkx

or::

   $ pip3 install networkx --user

Download and install Graphviz_ and ImageMagick_ from

   * http://www.graphviz.org/Download.php
   * http://www.imagemagick.org/script/binary-releases.php

Install |software| with *pip*::

   $ sudo pip3 install git+https://github.com/hklarner/PyBoolNet@2.31.0

which should place the package here::

   /usr/local/lib/python<version>/dist-packages/PyBoolNet

Use the option ``--user`` (literally) if you do not have sudo rights::

   $ pip3 install git+https://github.com/hklarner/PyBoolNet@2.31.0 --user

The package is likely going to be placed here::

   /home/<user>/.local/lib/python<version>/dist-packages/PyBoolNet

where ``<user>`` is the name you are logged in with (``$ whoami``) and ``<version>`` is the Python version you are using.

You should now be able to import |software|::

   $ python
   >>> import PyBoolNet

To remove |software| using *pip* run::

      $ pip3 uninstall PyBoolNet

If you do not have *pip*, all files must be removed manually.


Windows
-------
Download the latest release from

   * http://github.com/hklarner/PyBoolNet/releases

We recommend to install the package using *pip*. If it is not already shipped with your Python version follow the instructions
on

   * http://pip.pypa.io/en/latest/installing

To install |software| with *pip*::

   C:\> pip.exe install git+https://github.com/hklarner/PyBoolNet@2.31.0

which should place the package here::

   C:\Python<version>\Lib\site-packages

where ``<version>`` is the Python version you are using.

.. important::

   Make sure you check the paths to the executables. Locate the file ``settings.cfg`` in the ``Dependencies`` folder of your installation and
   try to run each program.

To install NetworkX_ use *pip* again::

   C:\> pip.exe install networkx

To install Graphviz_ and ImageMagick_ download the respective executables from the home pages:

   * http://www.graphviz.org/Download_windows.php
   * http://www.imagemagick.org/script/binary-releases.php#windows

You should now be able to import |software|::

   C:\> python
   >>> import PyBoolNet

To remove |software| using *pip* run::

      C:\> pip.exe uninstall PyBoolNet

If you do not have *pip*, all files must be removed manually.

Dependencies
------------

Most of what |software| does is written in pure Python but some crucial tasks, for example solving ASP problems or deciding CTL queries, are done using third party software.
The file that records the locations to third party binaries is called ``settings.cfg`` and located in the folder ``Dependencies`` of |software|.
The default location is::

   /usr/local/lib/python<version>/dist-packages/PyBoolNet/Dependencies/settings.cfg

The file is a standard configuration file of ``name = value`` pairs. The default for Linux 64 bit is::

   [Executables]
   nusmv           = ./NuSMV-a/NuSMVa_linux64
   gringo          = ./gringo-4.4.0/gringo_linux64
   bnet2prime      = ./BNetToPrime/BNetToPrime_linux64
   clasp           = ./clasp-3.1.1/clasp-3.1.1-x86_64-linux
   espresso        = ./espresso/espresso_linux64
   eqntott         = ./eqntott/eqntott_linux64
   dot             = /usr/bin/dot
   neato           = /usr/bin/neato
   fdp             = /usr/bin/fdp
   sfdp            = /usr/bin/sfdp
   circo           = /usr/bin/circo
   twopi           = /usr/bin/twopi
   convert         = /usr/bin/convert

If you want to use your own binaries simply replace the respective paths. Note that ``./`` indicates a relative path while ``/`` is an absolute path.
Make sure all these paths work and that rights for execution and access are set on linux systems.
To test whether the dependencies work correctly, run::

   $ python
   >>> import PyBoolNet
   >>> PyBoolNet.Tests.Dependencies.run()

If you get fails or errors, read :ref:`Troubleshooting <installation_troubleshooting>` and the issues section of the homepage:

   * http://github.com/hklarner/PyBoolNet/issues

where you can also post issues. Also, do not hesitate to contact me at |myemail|.


.. _installation_networkx:

NetworkX
........

NetworkX_ is a Python package and required for standard operations on directed graphs, e.g. computing strongly connected components,
deciding if a path between two nodes exists.
The package is available at:

   * http://networkx.github.io

To install it on Linux using *pip* run::

   $ sudo pip3 install networkx

or::

   $ pip3 install networkx --user

if you do not have super user rights.

.. _installation_bnettoprime:

BNetToPrime
...........

BNetToPrime_ stands for "Boolean network to prime implicants". It is necessary to compute the prime implicants of a Boolean network. It is included in every release and should work out of the box. The binaries and source are available at:

   * http://github.com/xstreck1/BNetToPrime


.. _installation_potassco:

Potassco
........

The Potassco answer set solving collection consists of the ASP solver clasp_ and the grounder gringo_, see :ref:`Gebser2011 <Gebser2011>`.
They are necessary to compute trap spaces by means of stable and consistent arc sets in the prime implicant graph, see :ref:`Klarner2015(a)<klarner2015trap>`. They are included in every release and should work out of the box.

.. note::
   The development of the Potassco solving collection is active with frequent releases.
   |software| is tested with two specific versions, clasp-3.1.1_ and gringo-4.4.0_ and we strongly recommend you use them because of syntax differences between versions.

The binaries and source are available at:

   * http://sourceforge.net/projects/potassco/files/clasp/3.1.1
   * http://sourceforge.net/projects/potassco/files/gringo/4.4.0


.. _installation_nusmv:

NuSMV
.....

NuSMV_ is a symbolic model checker that we use to decide LTL and CTL queries.
|software| requires the extension NuSMV-a_ for model checking with accepting states.
It is included with every release and should work out of the box.

.. note::
   |software| is tested with NuSMV-a_, an extension of NuSMV 2.6.0. If you do not need to compute accepting states you may use the regular NuSMV 2.6.0.

Binaries and source available at:

   * http://github.com/hklarner/NuSMV-a


.. _installation_graphviz:

Graphviz
........

The program *dot* is part of the graph visualization software Graphviz_ and available at

   * http://www.graphviz.org

It is required to generate drawings of interaction graphs and state transition graphs.
To install it on Linux run::

   $ sudo apt install graphviz

Make sure to check the paths in ``settings.cfg``.


.. _installation_imagemagick:

ImageMagick
...........

The program *convert* is part of the ImageMagick_ software suite.
It is required to generate animations of trajectories in the state transition graph.
To install it on linux run::

   $ sudo apt install ImageMagick

ImageMagick_ is available at

   * http://www.imagemagick.org

Make sure to check the paths in ``settings.cfg``.


.. _installation_matplotlib:

Matplotlib
..........

The package matplotlib is used to plot pie charts and bar plots and similiar graphs,
for example in the function :ref:`create_barplot` and :ref:`basins_create_piechart` of the :ref:`Basins` module.
To install it on linux run::

   $ sudo pip3 install matplotlib

matplotlib_ is available at

   * http://matplotlib.org



.. _installation_espresso:

Espresso
........

Espresso is required for heuristic minimization Boolean expressions.
For more information see

    * http://chmod755.tumblr.com/post/31417234230/espresso-heuristic-logic-minimizer


.. _installation_eqntott:

Eqntott
.......

Eqntott is required to converting Boolean expressions into the truth table format required by Espresso.
For more information see

    * https://code.google.com/archive/p/eqntott



Related Software
----------------

.. _installation_boolnet:

BoolNet
.......
BoolNet_ is a library for R_ that is used for the construction, simulation and analysis of Boolean networks, see :ref:`Müssel2010 <Müssel2010>`.
It is not a required dependency of |software| but you need it if you want to convert *SBML-qual* files into *bnet* files.
To install it run::

   $ sudo R
   > install.packages("BoolNet")

select a CRAN mirror and wait for the download and installation to finish.
BoolNet_ is available at

   * http://cran.r-project.org/web/packages/BoolNet/index.html


.. _installation_ginsim:

GINsim
......

GINsim_ is a Java program for the construction and analysis of qualitative regulatory and signaling networks, see :ref:`Chaouiya2012 <Chaouiya2012>`.
Like BoolNet_, GINsim_ is not a required dependency of |software| but it has a useful model repository. To convert GINsim_ models you need to export them as *SBML-qual* files which can then be converted into *bnet* files using BoolNet_.
No installation required, just download the latest version (tested with version 2.9) and call::

   $ java -jar GINsim-2.9.3.jar

GINsim_ is available at

   * http://www.ginsim.org


.. _installation_troubleshooting:

Troubleshooting
---------------

For questions that are not listed here please contact |myemail| or post an issue on the project homepage at

   * http://github.com/hklarner/PyBoolNet/issues


libreadline.so.6
................

If you get the error message::

   ./NuSMVa: error while loading shared libraries: libreadline.so.6:
   cannot open shared object file: No such file or directory

then a solution for linux is available at stackoverflow:

   * http://stackoverflow.com/questions/23993377/red-language-console-error-libreadline-so-6-cannot-open-shared-object-file

The crucial command::

   $ sudo apt install libreadline6:i386


permission denied
.................
If you get *permission denied* erros like::

   OSError: [Errno 13] Permission denied

you might have to change the mode of the files to make sure that they are executable.
Locate the directory that contains |Software| (see :ref:`Installation of PyBoolNet <installation_software>` above) and run::

   ../PyBoolNet$ chmod -R 744 Dependencies/
   ../PyBoolNet$ chmod -R +x Dependencies/
   ../PyBoolNet$


no such file or directory
.........................

If you get *No such file or directory* errors you might have installed the wrong package for your OS. In particular check whether you are on 32 bit or 64 bit Linux and download the respective files from:

   * http://github.com/hklarner/PyBoolNet/releases


.. include:: Substitutions.rst
