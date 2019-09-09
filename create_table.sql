create table if not exists `problems` (
    `id` INTEGER PRIMARY KEY autoincrement,
    `no` INT NOT NULL DEFAULT '0' UNIQUE, --COMMENT '题号'
    `hard` TINYINT NOT NULL DEFAULT '0', --COMMENT '1简单 2中等 3困难 4精通 5尝试',
    `title` VARCHAR(100) NOT NULL DEFAULT '', -- COMMENT '题目标题',
    `text` TEXT NOT NULL, -- COMMENT '题目描述',
    `total_commit` INT NOT NULL DEFAULT '0', -- '提交次数',
    `total_passed` INT NOT NULL DEFAULT '0' -- COMMENT '通过次数'
);

insert into problems values(NULL, 1, 4, "Quick-Sort", "Just sort a given random array.", 0, 0);
insert into problems values(NULL, 2, 4, "Binary Search", "Just find a number from sorted array.", 0, 0);