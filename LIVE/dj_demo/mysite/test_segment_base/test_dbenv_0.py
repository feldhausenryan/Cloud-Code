# Preserve the order, do "memp_trickle" test first
    def test_memp_2_sync(self) :
        self.db.put("hi", "bye")
        self.env.memp_sync()  # Full flush
        # Nothing to do...
        self.assertTrue(self.env.memp_trickle(100) == 0)
        self.db.put("hi", "bye2")
        self.env.memp_sync((1, 0))  # NOP, probably
        # Something to do... or not
        self.assertTrue(self.env.memp_trickle(100) >= 0)
        self.db.put("hi", "bye3")
        self.env.memp_sync((123, 99))  # Full flush
        # Nothing to do...
        self.assertTrue(self.env.memp_trickle(100) == 0)
