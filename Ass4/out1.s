.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-8($fp)
		li		 $s0,5
		sw		 $s0,-8($fp)
		lw		 $s0,-12($fp)
		lw		 $s1,-8($fp)
		move		 $s0,$s1
		sw		 $s0,-12($fp)
		lw		 $s0,-16($fp)
		li		 $s0,5
		sw		 $s0,-16($fp)
		lw		 $s0,-20($fp)
		li		 $s0,2
		sw		 $s0,-20($fp)
		lw		 $s0,-24($fp)
		lw		 $s1,-16($fp)
		lw		 $s2,-20($fp)
		sub		 $s0,$s1,$s2
		sw		 $s0,-24($fp)
		lw		 $s0,-28($fp)
		lw		 $s1,-12($fp)
		lw		 $s2,-24($fp)
		sub		 $s7,$s1,$s2
		slt		 $s6,$0,$s7
		slt		 $s5,$s7,$0
<<<<<<< HEAD
		or		 $s0,$s6,$s5
		sw		 $s0,-20($fp)
		lw		 $s0,-24($fp)
		lw		 $s1,-20($fp)
		li		 $s7,-1
		add		 $s0,$s1,$s7
		sw		 $s0,-24($fp)
		lw		 $s0,-24($fp)
		beq		 $s0,$0,L_0
		sw		 $s0,-24($fp)
=======
		nor		 $s0,$s6,$s5
		sw		 $s0,-28($fp)
		lw		 $s0,-28($fp)
		beq		 $s0,$0,L_0
		sw		 $s0,-28($fp)
>>>>>>> 3095d4df70b3facfb38e57e997d29a4f3eddd561
		lw		 $s1,-12($fp)
		move		 $a0,$s1
		li		 $v0,1
		syscall
		L_0:
		li		 $v0,10
		syscall
