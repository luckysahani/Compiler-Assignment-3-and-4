.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-20($fp)
		li		 $s0,2
		sw		 $s0,-20($fp)
		lw		 $s0,-20($fp)
		sw		 $s0,-8($sp)
		la		 $s0,-12($fp)
		sw		 $s0,-4($sp),####
		sw		 $s0,-12($sp)
		sw		 $s1,-16($sp)
		sw		 $s2,-20($sp)
		sw		 $ra,-24($sp)
		sw		 $fp,-28($sp)
		sw		 $sp,-32($sp)
		jal		 Main.HelloWorld.hi
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-24($fp)
		move		 $s0,$v0
		sw		 $s0,-24($fp)
		lw		 $s0,-28($fp)
		li		 $s0,0
		sw		 $s0,-28($fp)
		lw		 $s0,-28($fp)
		sw		 $s0,-8($sp)
		la		 $s0,-12($fp)
		sw		 $s0,-4($sp),####
		sw		 $s0,-12($sp)
		sw		 $s1,-16($sp)
		sw		 $s2,-20($sp)
		sw		 $ra,-24($sp)
		sw		 $fp,-28($sp)
		sw		 $sp,-32($sp)
		jal		 Main.HelloWorld.hp
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-32($fp)
		move		 $s0,$v0
		sw		 $s0,-32($fp)
		lw		 $s0,-36($fp)
		lw		 $s1,-24($fp)
		lw		 $s2,-32($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-36($fp)
		lw		 $s0,-40($fp)
		lw		 $s1,-36($fp)
		move		 $s0,$s1
		sw		 $s0,-40($fp)
		lw		 $s0,-44($fp)
		li		 $s0,2
		sw		 $s0,-44($fp)
		lw		 $s0,-48($fp)
		lw		 $s1,-40($fp)
		lw		 $s2,-44($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-48($fp)
		lw		 $s1,-48($fp)
		move		 $a0,$s1
		li		 $v0,1
		syscall
		jr		 $ra

Main.HelloWorld.hi:
		sub		 $fp,$sp,36
		lw		 $s7,-8($sp)
		sw		 $s7,-4($fp)
		lw		 $s7,-4($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		lw		 $s0,-12($fp)
		li		 $s0,4
		sw		 $s0,-12($fp)
		lw		 $s0,-16($fp)
		lw		 $s1,-12($fp)
		move		 $s0,$s1
		sw		 $s0,-16($fp)
		lw		 $s0,-20($fp)
		lw		 $s2,-16($fp)
		li		 $s7,4
		mult		 $s7,$s2
		mflo		 $s0
		sw		 $s0,-20($fp)
		lw		 $s0,-40($fp)
		li		 $s0,0
		sw		 $s0,-40($fp)
		lw		 $s0,-44($fp)
		lw		 $s1,-40($fp)
		move		 $s0,$s1
		sw		 $s0,-44($fp)
		lw		 $s0,-48($fp)
		li		 $s0,0
		sw		 $s0,-48($fp)
		lw		 $s0,-52($fp)
		lw		 $s1,-48($fp)
		move		 $s0,$s1
		sw		 $s0,-52($fp)
		lw		 $s0,-56($fp)
		li		 $s0,4
		sw		 $s0,-56($fp)
		lw		 $s0,-60($fp)
		la		 $s0,-24($fp),#3
		sw		 $s0,-60($fp)
		lw		 $s0,-68($fp)
		lw		 $s2,-52($fp)
		li		 $s7,4
		mult		 $s7,$s2
		mflo		 $s0
		sw		 $s0,-68($fp)
		lw		 $s0,-64($fp)
		lw		 $s1,-60($fp)
		lw		 $s2,-68($fp)
		sub		 $s0,$s1,$s2
		sw		 $s0,-64($fp)
		lw		 $s0,-64($fp)
		lw		 $s1,-56($fp)
		sw		 $s1,0($s0)
		sw		 $s0,-64($fp)
		lw		 $s0,-72($fp)
		li		 $s0,0
		sw		 $s0,-72($fp)
		lw		 $s0,-76($fp)
		lw		 $s1,-72($fp)
		move		 $s0,$s1
		sw		 $s0,-76($fp)
		L_0:
		lw		 $s0,-80($fp)
		li		 $s0,5
		sw		 $s0,-80($fp)
		lw		 $s0,-84($fp)
		lw		 $s1,-80($fp)
		lw		 $s2,-76($fp)
		sub		 $s7,$s1,$s2
		slt		 $s6,$0,$s7
		slt		 $s5,$s7,$0
		or		 $s0,$s6,$s5
		sw		 $s0,-84($fp)
		lw		 $s0,-84($fp)
		beq		 $s0,$0,L_3
		sw		 $s0,-84($fp)
		j		 L_1
		L_2:
		lw		 $s0,-76($fp)
		lw		 $s1,-76($fp)
		li		 $s7,1
		add		 $s0,$s1,$s7
		sw		 $s0,-76($fp)
		j		 L_0
		L_1:
		lw		 $s0,-44($fp)
		lw		 $s1,-44($fp)
		li		 $s7,1
		add		 $s0,$s1,$s7
		sw		 $s0,-44($fp)
		lw		 $s0,-88($fp)
		lw		 $s1,-76($fp)
		move		 $s0,$s1
		sw		 $s0,-88($fp)
		lw		 $s0,-92($fp)
		la		 $s0,-24($fp),#3
		sw		 $s0,-92($fp)
		lw		 $s0,-100($fp)
		lw		 $s2,-88($fp)
		li		 $s7,4
		mult		 $s7,$s2
		mflo		 $s0
		sw		 $s0,-100($fp)
		lw		 $s0,-96($fp)
		lw		 $s1,-92($fp)
		lw		 $s2,-100($fp)
		sub		 $s0,$s1,$s2
		sw		 $s0,-96($fp)
		lw		 $s0,-104($fp)
		lw		 $s1,-96($fp)
		lw		 $s0,0($s1)
		sw		 $s0,-104($fp)
		lw		 $s0,-108($fp)
		lw		 $s1,-44($fp)
		lw		 $s2,-104($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-108($fp)
		lw		 $s0,-44($fp)
		lw		 $s1,-108($fp)
		move		 $s0,$s1
		sw		 $s0,-44($fp)
		j		 L_2
		L_3:
		.data
		k_22:		 .asciiz "grabage\n" 
		.text
		la		 $a0,k_22
		li		 $v0,4
		syscall
		lw		 $s0,-44($fp)
		move		 $v0,$s0
		jr		 $ra
		jr		 $ra

Main.HelloWorld.hp:
		sub		 $fp,$sp,36
		lw		 $s7,-8($sp)
		sw		 $s7,-4($fp)
		lw		 $s7,-4($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		.data
		k_0:		 .asciiz "\nHelloWorld\n" 
		.text
		la		 $a0,k_0
		li		 $v0,4
		syscall
		lw		 $s0,-4($fp)
		move		 $v0,$s0
		jr		 $ra
		jr		 $ra
