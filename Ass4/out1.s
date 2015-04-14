.data
newline : .asciiz "\n"
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-8($fp)
		li		 $s0,0
		sw		 $s0,-8($fp)
		lw		 $s0,-12($fp)
		lw		 $s1,-8($fp)
		move		 $s0,$s1
		sw		 $s0,-12($fp)
		L_0:
		lw		 $s0,-16($fp)
		li		 $s0,1
		sw		 $s0,-16($fp)
		lw		 $s0,-20($fp)
		lw		 $s1,-12($fp)
		lw		 $s2,-16($fp)
		add		 $s0,$s1,$s2
		sw		 $s0,-20($fp)
		lw		 $s0,-12($fp)
		lw		 $s1,-20($fp)
		move		 $s0,$s1
		sw		 $s0,-12($fp)
		lw		 $s0,-24($fp)
		li		 $s0,6
		sw		 $s0,-24($fp)
		lw		 $s0,-28($fp)
		lw		 $s1,-12($fp)
		lw		 $s2,-24($fp)
		slt		 $s0,$s1,$s2
		sw		 $s0,-28($fp)
		lw		 $s0,-28($fp)
		bne		 $s0,$0,L_0
		.data
		k_6:		 .asciiz "Good Job " 
		.text
		la		 $a0,k_6
		li		 $v0,4
		syscall
		la		 $a0,newline
		li		 $v0,4
		syscall
		lw		 $s1,-12($fp)
		move		 $a0,$s1
		li		 $v0,1
		syscall
		li		 $v0,10
		syscall
