.data
.text
main:
Main.HelloWorld.main:
		sub		 $sp,$sp,200
		la		 $fp,200($sp)
		li		 $t0,0
		move		 $t1,$t0
		li		 $t2,10
		move		 $t4,$t2
		li		 $t5,50
		mult		 $t4,$t5
		mflo		 $t6
		li		 $s7,4
		mult		 $s7,$t6
		mflo		 $t7
		li		 $s0,1
		li		 $s1,2
		move		 $s2,$s0
		mult		 $t5,$s2
		mflo		 $s4
		add		 $s5,$s4,$s1
		li		 $s6,15
		sw		 $t0,-4($fp)
		add		 $s7,$s5,$t0
		li		 $s7,4
		mult		 $s7,$s7
		mflo		 $t0

Main:
