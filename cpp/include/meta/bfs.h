#ifndef BFS_H
#define BFS_H

#include <iostream>
#include <utility>
#include <vector>
#include <unordered_map>
#include <gsl/gsl>

struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const std::pair<T1, T2>& p) const{
        return std::hash<T1>()(p.first) ^ std::hash<T2>()(p.second);
    }
};

namespace Planning {

    using Point = std::pair<int, int>;

    template <typename Env>
    class Bfs {
        public:
        Bfs(std::shared_ptr<Env> _env);
        ~Bfs();

        bool plan( Point _start, Point _goal );
        void printVistedNodes();

        private:
        std::shared_ptr<Env> m_env;
        std::vector<Point> m_queue;
        std::unordered_map< Point, bool, hash_pair > m_closed;
    };

    template <typename Env>
    Bfs<Env>::Bfs(std::shared_ptr<Env> _env){
        m_env = _env;
    }

    template <typename Env>
    Bfs<Env>::~Bfs(){}

    template <typename Env>
    bool Bfs<Env>::plan( Point _start, Point _goal ){
            m_queue.clear();
            m_closed.clear();
            m_queue.push_back(_start);
            gsl::index idx = 0;
            Point curr_pt = m_queue[idx];
            while( curr_pt != _goal && (idx < m_queue.size()) ){
                auto succs = m_env->Succs(curr_pt);
                for( auto succ: succs ){
                    if(!m_closed.count(succ)){
                        m_queue.push_back(succ);
                        m_closed[succ] = 1;
                    }
                }
                idx++;
                curr_pt = m_queue[idx];
            }
            if(idx >= m_queue.size())
                return false;
            return true;
        }

    template <typename Env>
        void Bfs<Env>::printVistedNodes(){
            for(auto& pt: m_queue){
                std::cout<<pt.first<<"  "<<pt.second<<"\n";
            }
            std::cout<<"Total "<<m_queue.size()<<" nodes visited\n";
        }
}// namespace Planning

#endif /* ifndef BFS_H*/
