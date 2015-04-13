.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-4($fp)
		li		 $s0,0
		sw		 $s0,-4($fp)
		lw		 $s0,-0($fp)
		lw		 $s1,-4($fp)
		move		 $s0,$s1
		sw		 $s0,-0($fp)
		lw		 $s0,-8($fp)
		li		 $s0,0
		sw		 $s0,-8($fp)
		lw		 $s0,-12($fp)
		lw		 $s1,-8($fp)
		move		 $s0,$s1
		sw		 $s0,-12($fp)
		L_0:
		lw		 $s0,-16($fp)
		li		 $s0,15
		sw		 $s0,-16($fp)
		lw		 $s0,-20($fp)
		lw		 $s1,-12($fp)
		lw		 $s2,-16($fp)
		slt		 $s0,$s1,$s2
		sw		 $s0,-20($fp)
		lw		 $s0,-20($fp)
		beq		 $s0,$0,L_3
		sw		 $s0,-20($fp)
		j		 L_1
		L_2:
		lw		 $s0,-12($fp)
		lw		 $s1,-12($fp)
		li		 $s7,1
		add		 $s0,$s1,$s7
		sw		 $s0,-12($fp)
		j		 L_0
		L_1:
		lw		 $s0,-24($fp)
		lw		 $s1,-0($fp)
		lw		 $s2,-12($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-24($fp)
		lw		 $s0,-0($fp)
		lw		 $s1,-24($fp)
		move		 $s0,$s1
		sw		 $s0,-0($fp)
		j		 L_2
		L_3:
		lw		 $s0,-28($fp)
		li		 $s0,15
		sw		 $s0,-28($fp)
		lw		 $s0,-0($fp)
		sw		 $s0,-4($sp)
		lw		 $s0,-0($fp)
		sw		 $s0,-8($sp)
		lw		 $s0,-0($fp)
		sw		 $s0,-12($sp)
		lw		 $s0,-28($fp)
		sw		 $s0,-16($sp)
		sw		 $s0,-20($sp)
		sw		 $s1,-24($sp)
		sw		 $s2,-28($sp)
		sw		 $ra,-32($sp)
		sw		 $fp,-36($sp)
		jal		 Main.HelloWorld.printv
		li		 $v0,10
		syscall

Main:

Main.HelloWorld.printv:
		sub		 $fp,$sp,40
		lw		 $s7,-4($sp)
		sw		 $s7,0($fp)
		lw		 $s7,-8($sp)
		sw		 $s7,-4($fp)
		lw		 $s7,-12($sp)
		sw		 $s7,-8($fp)
		lw		 $s7,-16($sp)
		sw		 $s7,-12($fp)
		sub		 $sp,$fp,400
		lw		 $s0,-16($fp)
		lw		 $s1,-0($fp)
		lw		 $s2,-4($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-16($fp)
		lw		 $s0,-20($fp)
		lw		 $s1,-16($fp)
		lw		 $s2,-8($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-20($fp)
		lw		 $s0,-24($fp)
		lw		 $s1,-20($fp)
		lw		 $s2,-12($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-24($fp)
		lw		 $s0,-28($fp)
		lw		 $s1,-24($fp)
		move		 $s0,$s1
		sw		 $s0,-28($fp)
		lw		 $s1,-28($fp)
		move		 $a0,$s1
		li		 $v0,1
		syscall
		jr		 $ra
