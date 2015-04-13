.data
.text
main:
Main.HelloWorld.main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		li		 $t0,10
		move		 $t1,$t0
		li		 $t2,9
		move		 $t3,$t2
		slt		 $t4,$t1,$t3
		move		 $t5,$t4
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
		sw		 $ra,-64($sp)
		sw		 $fp,-68($sp)
		jal		 bool

Main:
