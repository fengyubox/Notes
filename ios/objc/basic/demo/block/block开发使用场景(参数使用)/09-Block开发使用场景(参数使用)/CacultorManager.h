//
//  CacultorManager.h
//  09-Block开发使用场景(参数使用)
//
//  Created by xiaomage on 16/3/9.
//  Copyright © 2016年 小码哥. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface CacultorManager : NSObject

@property (nonatomic, assign) NSInteger result;

// 计算
- (void)cacultor:(NSInteger(^)(NSInteger result))cacultorBlock;

@end
