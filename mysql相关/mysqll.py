#!/usr/bin/env python
#_*_coding:utf-8_*_

import logging
import MySQLdb
from comm_log_record import record_log_init

class _MySQL(object):
    def __init__(self, host, user, passwd, db, charset='utf8'):
        self.conn = MySQLdb.connect(
                host = host,
                user = user,
                passwd = passwd,
                db = db,
                charset = charset)
    def get_cursor(self):
        return self.conn.cursor()

    def query(self, sql):
        cursor = self.get_cursor()  
        try:
            cursor.execute(sql, None)
            result = cursor.fetchall()  
        except Exception, e:
            logging.error("mysql query error: %s", e)
            return None
        finally:
            cursor.close()
        return result

    def execute(self, sql, param=None):
        cursor = self.get_cursor()
        try:
            cursor.execute(sql, param)
            self.conn.commit()
            affected_row = cursor.rowcount
        except Exception, e:
            logging.error("mysql execute error: %s", e)
            return 0
        finally:
            cursor.close()
        return affected_row

    def executemany(self, sql, params=None):
        cursor = self.get_cursor()
        try:
            cursor.executemany(sql, params)
            self.conn.commit()
            affected_rows = cursor.rowcount
        except Exception, e:
            logging.error("mysql executemany error: %s", e)
            return 0
        finally:
            cursor.close()
        return affected_rows

    def close(self):
        try:
            self.conn.close()
        except:
            pass

    def __del__(self):
        self.close()


def main():
    host = 'localhost'
    user = 'root'
    passwd = '123456'
    db = 'mdss'
    mysql = _MySQL(host, user, passwd, db)

    logger = record_log_init()

    params = ['s_dns_rdnsdcnt',
              's_dns_unregdomainscnt',
              's_dns_maldomainsdetail',
              's_dns_malnxdomainsdetail',
              's_traffic_protocols_hour',
              's_traffic_ips_hour',
              's_dns_topdomainsdcnt',
              's_dns_topipdomains',
              's_traffic_protocols_ips_day',
              's_dns_maldomainscnt'
              ]

    param_t = ['s_dns_newDomainslist',
               's_dns_newdomainslist',
               's_url_topdownloaddcnt',
               's_url_topattackdesthcnt',
               's_dns_areahcnt',
               's_url_topmalshcnt',
               's_url_topattacksrchcnt',
               's_dns_passivedomaintamper',
               's_dns_topabdomainshcnt',
              ]

    param_T = ['c_dns_newiplist']

    param_C = ['s_url_topdownlinkhcnt','s_url_topuplinkhcnt','s_url_topdownlinkhcnt']
    
    param_B = ['i_ddos_attackers']

    for dname in params:
        cmd = 'ALTER TABLE %s partition by range(year(date)*100+month(date))(partition p5 values less than (201612),partition p6 values less than (201712));' %dname
        print 'Start %s' %dname
        logger.info('Start %s' %dname)
        ret1 = mysql.execute(cmd)
        print 'End %s' %dname
        logger.info('End %s : %s' %(ret1,dname))
    ''' 
    for dname in param_t:
        cmd = 'ALTER TABLE %s partition by range(year(time)*100+month(time))(partition p1 values less than (201610),partition p2 values less than (201611),partition p3 values less than (205301));' %dname
        print 'Start %s' %dname
        logger.info('Start %s' %dname)
        ret2 = mysql.execute(cmd)
        print 'End %s' %dname
        logger.info('End %s : %s' %(ret2,dname))

    for dname in param_T:
        cmd = 'ALTER TABLE %s partition by range(year(Time)*100+month(Time))(partition p1 values less than (201610),partition p2 values less than (201611),partition p3 values less than (205301));' %dname
        print 'Start %s' %dname
        logger.info('Start %s' %dname)
        ret3 = mysql.execute(cmd)
        print 'End %s' %dname
        logger.info('End %s : %s' %(ret3,dname))
        
    for dname in param_B:
        cmd = 'ALTER TABLE %s partition by range(year(begin_time)*100+month(begin_time))(partition p1 values less than (201610),partition p2 values less than (201611),partition p3 values less than (205301));' %dname
        print 'Start %s' %dname
        logger.info('Start %s' %dname)
        ret33 = mysql.execute(cmd)
        print 'End %s' %dname
        logger.info('End %s : %s' %(ret33,dname))

    for dname in param_C:
        cmd = 'ALTER TABLE %s partition by range(year(Createtime)*100+month(Createtime))(partition p1 values less than (201610),partition p2 values less than (201611),partition p3 values less than (205301));' %dname
        print 'Start %s' %dname
        logger.info('Start %s' %dname)
        ret4 = mysql.execute(cmd)
        print 'End %s' %dname
        logger.info('End %s : %s' %(ret4,dname))
   ''' 

if __name__ == '__main__':
    main()
