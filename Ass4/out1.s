.data
.text
main:
Main.HelloWorld.main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-4($fp)
		li		 $s0,9
		sw		 $s0,-4($fp)
		lw		 $s0,-4($fp)
		sw		 $s0,-8($sp)
		sw		 $s0,-12($sp)
		sw		 $s1,-16($sp)
		sw		 $s2,-20($sp)
		sw		 $ra,-24($sp)
		sw		 $fp,-28($sp)
		sw		 $sp,-32($sp)
		jal		 Main.HelloWorld.func
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-8($fp)
		move		 $s0,$v0
		sw		 $s0,-8($fp)
		li		 $v0,10
		syscall

Main:

Main.HelloWorld.func:
		sub		 $fp,$sp,36
		lw		 $s7,-8($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		.data
		k_0:		 .asciiz "Good Job Archit\n" 
		.text
		la		 $a0,k_0
		li		 $v0,4
		syscall
		jr		 $ra
