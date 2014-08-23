Context Free Animator Documentation
===================================

This file describes the process of creating a .cfda file that can be used
by the Context Free Animator to create an animation.

For information on command line syntax see 'usage.txt'.

For a gallery of animations created using the Context Free Animator
visit: http://www.goshdarngames.com/context-free-animator-gallery/

This document assumes working knowledge of Context Free Art.  For information
on how to use Context Free Art visit:
    http://www.contextfreeart.org/mediawiki/index.php/CFDG_HOWTO
    
If you're stuck, consider posting a question on the Context Free Forums:
    http://www.contextfreeart.org/phpbb/index.php
    
How Does Context Free Animator work?
====================================

Context Free Animator (CFA) accepts as input a CFDA file.

For each frame of animation CFA parses the CFDA file and generates
a CFDG file that it passes to Context Free for rendering.

CFA produces a PNG for each frame of the animation, which is saved
in the output directory specified by the user. 
    
What is a CFDA?
===============

CFDA files are the same as CFDG files except they contain special
operations used in animation.  For each frame of animation Context Free
Animator parses these special operations and then sends the parsed file
to Context Free for rendering.

The special operations are surrounded by # symbols.  These operations
specify text to be replaced by the Context Free Animator when it is
parsing the file.

What Are The Special Operations?
================================

Only one operation has been implemented so far:

    - #add, (initial_value), (amount)#
    
      When the cfda is parsed by Context Free Animator this opcode will
      be replaced by a number (lets call the number X).
      
      On the first frame X will be equal to 'initial_value'.
      
      On each subsequent frame X will increase by 'amount'.
      
      'initial_value' and 'amount' can be any floating point number
      (including negative numbers)
      
      So if the operation #add, 0, 10# appears in a CFDA file it will
      be replaced by 0 in the first frame, 10 in the second and 20
      in the third and so on.  

Example CFDA File:
==================

Here is an example CFDA file that generates a rotating square:

------------------------------------------------------------------------------

    startshape START[] //The shape to render first
    CF::Size = [s 2] //The size of the canvas.  Explained below

    shape START
    {
        SQUARE[r #add,0,9#] //A call to draw a square with a CFA operation
    }

------------------------------------------------------------------------------

CFDA files are the same as CFDG files except the contain special operations
used in animation.

This CFDA file starts with the shape named START.

We set the environment variable CF::Size to [s 2].  We do this because
Context Free automatically resizes the canvas to fit all shapes in. 
By setting a fixed size for the canvas all the frames of our animation
will be aligned and the same size.  When creating an animation that will
change the size of the canvas make sure and set CF::Size to a value big 
enough to hold all frames of the animation.

The start shape will draw a SQUARE.  We specify that its rotation should
change with each frame:  [r #add,0,9#]

The operation specifies that the rotation should start at zero and increase
by 9 each frame.  This means that if we generate 10 frames of animation
using CFA we will have enough frames to create a looping animation.

      