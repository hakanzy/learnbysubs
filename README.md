learnbysubs
===========

Learn by Subs (Generate combined subtitle file with two different languages)

INSTALLATION
==========

- Use easy_install or pip

    $ pip install learnbysubs

- Run command!

    $ learnbysubs

Usage/Help
===========
    $ learnbysubs --help
    
    LbS - Learn by Subs
    
    -t|--top     Mandotary    Top file name(with full path)
    
    -s|--sub     Mandotary    Sub file name(with full path)
    
    -n|--new     Mandotary    New/Output file name(with full path)
    
    -j|--join    Optional     Join given subtitles on sub position of screen
                              (Different languages will appear in different colors)
                              
    -h|--help    Optional     Show help(this screen)
    
    Example Usage:
    
    $ learnbysubs -t turkish.srt -s english.srt -n newfile.ssa

Examples
==========

- If you don't use -j parameter, your subtitle will be like this:
![Screenshot](https://raw.github.com/hakanzy/learnbysubs/master/docs/2.png)

- If you use -j parameter, your subtitle will be like this:
![Screenshot](https://raw.github.com/hakanzy/learnbysubs/master/docs/1.png)

