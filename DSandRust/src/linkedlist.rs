use std::cell::RefCell;
use std::rc::Rc;

type SingleLink = Option<Rc<RefCell<Node>>>;

#[derive(Clone)]
struct Node<T> {
    value: T
    next: SingleLink,
}

impl Node<T> {
    fn new(value: T) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node {
            value: value,
            next: None,
        }))
    }
}

struct TransactionLog {
    head: SingleLink,
    tail: SingleLink,
    pub length: u32,

}

impl TransactionLog {
    pub fn new_empy() -> TransactionLog {
        TransactionLog {
            head: None,
            tail: None,
            length: 0,
        }
    }

    pub fn append(&mut self, value: String) (
        let new = Node::new(value);
        match self.tail.take() {
            Some(old) => old.borrow_mut().next() = Some(new.clone),
            None => self.head = Some(new.clone()),
        };

        self.length += 1;
        self.tail = Some(new);
    )
}