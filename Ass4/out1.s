.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		sw		 $s0,-8($sp)
		sw		 $s1,-12($sp)
		sw		 $s2,-16($sp)
		sw		 $ra,-20($sp)
		sw		 $fp,-24($sp)
		sw		 $sp,-28($sp)
		jal		 Main.CallingMethodsInSameClass.printOne
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-4($fp)
		move		 $s0,$v0
		sw		 $s0,-4($fp)
		sw		 $s0,-8($sp)
		sw		 $s1,-12($sp)
		sw		 $s2,-16($sp)
		sw		 $ra,-20($sp)
		sw		 $fp,-24($sp)
		sw		 $sp,-28($sp)
		jal		 Main.CallingMethodsInSameClass.printOne
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-8($fp)
		move		 $s0,$v0
		sw		 $s0,-8($fp)
		sw		 $s0,-8($sp)
		sw		 $s1,-12($sp)
		sw		 $s2,-16($sp)
		sw		 $ra,-20($sp)
		sw		 $fp,-24($sp)
		sw		 $sp,-28($sp)
		jal		 Main.CallingMethodsInSameClass.printTwo
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-12($fp)
		move		 $s0,$v0
		sw		 $s0,-12($fp)
		jr		 $ra

Main.CallingMethodsInSameClass.printOne:
		sub		 $fp,$sp,32
		lw		 $s7,-4($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		.data
		k_0:		 .asciiz "Hello World" 
		.text
		la		 $a0,k_0
		li		 $v0,4
		syscall
		jr		 $ra

Main.CallingMethodsInSameClass.printTwo:
		sub		 $fp,$sp,32
		lw		 $s7,-4($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		sw		 $s0,-8($sp)
		sw		 $s1,-12($sp)
		sw		 $s2,-16($sp)
		sw		 $ra,-20($sp)
		sw		 $fp,-24($sp)
		sw		 $sp,-28($sp)
		jal		 Main.CallingMethodsInSameClass.printOne
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-4($fp)
		move		 $s0,$v0
		sw		 $s0,-4($fp)
		sw		 $s0,-8($sp)
		sw		 $s1,-12($sp)
		sw		 $s2,-16($sp)
		sw		 $ra,-20($sp)
		sw		 $fp,-24($sp)
		sw		 $sp,-28($sp)
		jal		 Main.CallingMethodsInSameClass.printOne
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-8($fp)
		move		 $s0,$v0
		sw		 $s0,-8($fp)
		jr		 $ra
