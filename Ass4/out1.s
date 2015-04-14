.data
.text
main:
Main.HelloWorld.main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		.data
		k_0:		 .asciiz "Hello" 
		.text
		.data
		s:		 .asciiz "Hello" 
		.text
		la		 $a0,s
		li		 $v0,4
		syscall
		li		 $v0,10
		syscall

Main:
