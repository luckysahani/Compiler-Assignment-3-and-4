.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-4($fp)
		li		 $s0,30
		sw		 $s0,-4($fp)
		lw		 $s0,-8($fp)
		lw		 $s1,-4($fp)
		move		 $s0,$s1
		sw		 $s0,-8($fp)
		lw		 $s0,-12($fp)
		li		 $s0,10
		sw		 $s0,-12($fp)
		lw		 $s0,-16($fp)
		lw		 $s1,-8($fp)
		lw		 $s2,-12($fp)
		sub		 $s7,$s1,$s2
		slt		 $s6,$0,$s7
		slt		 $s5,$s7,$0
		or		 $s0,$s6,$s5
		li		 $s7,1
		sub		 $s0,$s7,$s0
		sw		 $s0,-16($fp)
		lw		 $s0,-16($fp)
		beq		 $s0,$0,L_0
		.data
		k_4:		 .asciiz "Value of X is 10" 
		.text
		la		 $a0,k_4
		li		 $v0,4
		syscall
		j		 L_1
		L_0:
		.data
		k_7:		 .asciiz "This is else statement" 
		.text
		la		 $a0,k_7
		li		 $v0,4
		syscall
		L_1:
		jr		 $ra
