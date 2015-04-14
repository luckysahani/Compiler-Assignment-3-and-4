.data
.text
main:
Main.fin.main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		lw		 $s0,-8($fp)
		li		 $s0,10
		sw		 $s0,-8($fp)
		lw		 $s0,-8($fp)
		sw		 $s0,-8($sp)
		la		 $s0,-4($fp)
		sw		 $s0,-4($sp),####
		sw		 $s0,-12($sp)
		sw		 $s1,-16($sp)
		sw		 $s2,-20($sp)
		sw		 $ra,-24($sp)
		sw		 $fp,-28($sp)
		sw		 $sp,-32($sp)
		jal		 Main.fibo.fib
		lw		 $ra,12($fp)
		lw		 $sp,4($fp)
		lw		 $fp,8($fp)
		lw		 $s0,-12($fp)
		move		 $s0,$v0
		sw		 $s0,-12($fp)
		lw		 $s0,-16($fp)
		lw		 $s1,-12($fp)
		move		 $s0,$s1
		sw		 $s0,-16($fp)
		lw		 $s1,-16($fp)
		move		 $a0,$s1
		li		 $v0,1
		syscall
		jr		 $ra

Main:

Main.fibo.fib:
		sub		 $fp,$sp,36
		lw		 $s7,-8($sp)
		sw		 $s7,0($fp)
		sub		 $sp,$fp,400
		lw		 $s0,-8($fp)
		li		 $s0,5
		sw		 $s0,-8($fp)
		lw		 $s0,-4($fp)
		lw		 $s1,-8($fp)
		move		 $s0,$s1
		sw		 $s0,-4($fp)
		lw		 $s0,-12($fp)
		move		 $v0,$s0
		jr		 $ra
		jr		 $ra
