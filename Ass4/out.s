.data
.text
main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		li		 $t0,10
		move		 $t1,$t0
		li		 $t2,15
		move		 $t4,$t2
		move		 $a0,$t1
		move		 $a1,$t4
		jal		 Main.HelloWorld.add
		move		 $t5,$t6
		add $s3,$0,$v0
		move $a0,$s3
	    li $v0,1
	    syscall
		li $v0,10
		syscall

Main.HelloWorld.add:
		sw		 $t0,-4($sp)
		sw		 $t1,-8($sp)
		sw		 $t2,-12($sp)
		sw		 $t3,-16($sp)
		sw		 $t4,-20($sp)
		sw		 $t5,-24($sp)
		sw		 $t6,-28($sp)
		sw		 $t7,-32($sp)
		sw		 $s0,-36($sp)
		sw		 $s1,-40($sp)
		sw		 $s2,-44($sp)
		sw		 $s3,-48($sp)
		sw		 $s4,-52($sp)
		sw		 $s5,-56($sp)
		sw		 $s6,-60($sp)
		sw		 $s7,-64($sp)
		sw		 $ra,-68($sp)
		sw		 $fp,-72($sp)
		sub		 $sp,$sp,276
		add		 $t7,$a0,$a1
		move		 $s2,$t7
		move		 $v0,$s2
		jr		 $ra
